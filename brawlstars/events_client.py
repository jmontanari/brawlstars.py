# coding: utf-8

"""
    Brawl Stars API - EventsClient

    Extended client with background polling and event dispatching capabilities.

    Example usage:
        import brawlstars

        client = brawlstars.EventsClient()
        client.login_with_token("your_token")

        @client.event
        @brawlstars.ClubEvents.member_join()
        async def on_member_join(member, club):
            print(f"{member.name} joined {club.name}")

        client.add_club_updates("#CLUB_TAG")
        client.run_forever()
"""

import asyncio
import logging
import traceback
from datetime import datetime, timezone
from typing import Callable, Dict, Optional, Set

from brawlstars.client.brawl_client import BrawlClient
from brawlstars.models.club import Club
from brawlstars.models.player import Player
from brawlstars.events import Event
from brawlstars.errors import Maintenance
from brawlstars.utils import correct_tag
from brawlstars.exceptions import ServiceException

LOG = logging.getLogger(__name__)
DEFAULT_SLEEP = 10


class EventsClient(BrawlClient):
    """Extended BrawlClient with event polling capabilities.

    This client extends the base BrawlClient to add:
    - Background polling tasks for clubs and players
    - Event registration and dispatching
    - Maintenance detection and handling
    - In-memory caching for change detection

    Parameters
    ----------
    loop : asyncio.AbstractEventLoop, optional
        The event loop to use. If not provided, uses the current running loop.
    club_retry_interval : int, optional
        Minimum seconds between club update checks. Default is 0 (use API rate).
    player_retry_interval : int, optional
        Minimum seconds between player update checks. Default is 0 (use API rate).
    club_cls : class, optional
        Custom Club class for deserialization. Default is Club.
    player_cls : class, optional
        Custom Player class for deserialization. Default is Player.

    Example
    -------
    >>> import asyncio
    >>> import brawlstars
    >>>
    >>> client = brawlstars.EventsClient()
    >>> client.login_with_token("your_token")
    >>>
    >>> @client.event
    >>> @brawlstars.ClubEvents.member_join()
    >>> async def on_member_join(member, club):
    ...     print(f"{member.name} joined {club.name}")
    >>>
    >>> client.add_club_updates("#2PP")
    >>> client.run_forever()
    """

    def __init__(self, loop: Optional[asyncio.AbstractEventLoop] = None, **options):
        super().__init__()

        self.loop = loop or asyncio.new_event_loop()
        self._setup()

        self._in_maintenance_event = asyncio.Event()
        self._in_maintenance_event.set()  # Only block when maintenance is on

        self.club_retry_interval = options.pop("club_retry_interval", 0)
        self.player_retry_interval = options.pop("player_retry_interval", 0)

        self.club_cls = options.pop("club_cls", Club)
        self.player_cls = options.pop("player_cls", Player)

        self.club_loops_run = 0
        self.player_loops_run = 0

        self._locks: Dict[str, asyncio.Lock] = {}

    def _setup(self):
        """Initialize updater tasks and caches."""
        self._updater_tasks = {
            "club": self.loop.create_task(self._club_updater()),
            "player": self.loop.create_task(self._player_updater()),
            "maintenance": self.loop.create_task(self._maintenance_poller()),
        }

        for task in self._updater_tasks.values():
            task.add_done_callback(self._task_callback_check)

        self._club_updates: Set[str] = set()
        self._player_updates: Set[str] = set()

        self._listeners = {"club": [], "player": [], "client": {}}

        self._clubs: Dict[str, Club] = {}
        self._players: Dict[str, Player] = {}

    # -------------------------------------------------------------------------
    # Tag Subscription Methods
    # -------------------------------------------------------------------------

    def add_club_updates(self, *tags: str):
        """Add club tags to receive updates for.

        Parameters
        ----------
        *tags : str
            The club tags to add. If you wish to pass in an iterable,
            you must unpack it with *.

        Example
        -------
        >>> client.add_club_updates("#TAG1", "#TAG2", "#TAG3")
        >>> tags = ["#TAG4", "#TAG5"]
        >>> client.add_club_updates(*tags)
        """
        for tag in tags:
            if not isinstance(tag, str):
                raise TypeError(f"club tag must be of type str not {tag!r}")
            self._club_updates.add(correct_tag(tag))

    def remove_club_updates(self, *tags: str):
        """Remove club tags from receiving updates.

        Parameters
        ----------
        *tags : str
            The club tags to remove.
        """
        for tag in tags:
            if not isinstance(tag, str):
                raise TypeError(f"club tag must be of type str not {tag!r}")
            try:
                self._club_updates.remove(correct_tag(tag))
            except KeyError:
                pass

    def add_player_updates(self, *tags: str):
        """Add player tags to receive updates for.

        Parameters
        ----------
        *tags : str
            The player tags to add.

        Example
        -------
        >>> client.add_player_updates("#PLAYER1", "#PLAYER2")
        """
        for tag in tags:
            if not isinstance(tag, str):
                raise TypeError(f"player tag must be of type str not {tag!r}")
            self._player_updates.add(correct_tag(tag))

    def remove_player_updates(self, *tags: str):
        """Remove player tags from receiving updates.

        Parameters
        ----------
        *tags : str
            The player tags to remove.
        """
        for tag in tags:
            if not isinstance(tag, str):
                raise TypeError(f"player tag must be of type str not {tag!r}")
            try:
                self._player_updates.remove(correct_tag(tag))
            except KeyError:
                pass

    # -------------------------------------------------------------------------
    # Cache Methods
    # -------------------------------------------------------------------------

    def _get_cached_club(self, tag: str) -> Optional[Club]:
        return self._clubs.get(tag)

    def _update_club(self, club: Club):
        self._clubs[club.tag] = club

    def _get_cached_player(self, tag: str) -> Optional[Player]:
        return self._players.get(tag)

    def _update_player(self, player: Player):
        self._players[player.tag] = player

    # -------------------------------------------------------------------------
    # Event Registration
    # -------------------------------------------------------------------------

    def event(self, function: Callable):
        """A decorator or regular function that registers an event.

        The function must be a coroutine.

        Parameters
        ----------
        function : coroutine
            The function to be registered.

        Example
        -------
        >>> @client.event
        >>> @brawlstars.ClubEvents.member_join()
        >>> async def on_member_join(member, club):
        ...     print(f"{member.name} joined {club.name}")

        Note
        ----
        The order of decorators is important - @client.event must be above
        the event type decorator.

        Returns
        -------
        function
            The registered function.
        """
        if getattr(function, "is_client_event", False):
            try:
                self._listeners["client"][function.event_name].append(function)
            except KeyError:
                self._listeners["client"][function.event_name] = [function]
            return function

        if not getattr(function, "is_event_listener", None):
            raise ValueError("no events found to register to this callback")

        events = [Event.from_decorator(function, runner) for runner in function.event_runners]

        retry_interval = getattr(function, "event_retry_interval", None)
        cls = getattr(function, "event_cls", None)
        tags = getattr(function, "event_tags", ())
        event_type = events[0].type

        self._listeners[event_type].extend(events)

        if event_type == "club":
            self.club_cls = cls or self.club_cls
            self.club_retry_interval = retry_interval or self.club_retry_interval
            self.add_club_updates(*tags)
        elif event_type == "player":
            self.player_cls = cls or self.player_cls
            self.player_retry_interval = retry_interval or self.player_retry_interval
            self.add_player_updates(*tags)

        LOG.info("Successfully registered %s event", function)
        return function

    def add_events(self, *events: Callable):
        """Shortcut to add many events at once.

        Parameters
        ----------
        *events : function
            The event listener functions to add.
        """
        for event in events:
            self.event(event)

    def remove_events(self, *events: Callable):
        """Shortcut to remove many events at once.

        Parameters
        ----------
        *events : function
            The event listener functions to remove.
        """
        for function in events:
            for runner in function.event_runners:
                event = Event.from_decorator(function, runner)
                self._listeners[event.type].remove(event)

    # -------------------------------------------------------------------------
    # Event Dispatching
    # -------------------------------------------------------------------------

    def dispatch(self, event_name: str, *args, **kwargs):
        """Dispatch a client event.

        Parameters
        ----------
        event_name : str
            The name of the event to dispatch.
        *args, **kwargs
            Arguments to pass to the event callbacks.
        """
        registered = self._listeners["client"].get(event_name)
        if registered is None:
            if event_name == "event_error":
                LOG.exception("Ignoring exception in event task.")
                traceback.print_exc()
        else:
            for event in registered:
                try:
                    asyncio.ensure_future(event(*args, **kwargs), loop=self.loop)
                except Exception:
                    LOG.exception("Ignoring exception in %s.", event_name)

    # -------------------------------------------------------------------------
    # Lifecycle Methods
    # -------------------------------------------------------------------------

    def run_forever(self):
        """A blocking call which runs the loop and script.

        This is useful if you have no other clients to deal with and
        just wish to run the script and receive updates indefinitely.

        Example
        -------
        >>> client.run_forever()
        """
        try:
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.close()

    def close(self):
        """Close the client and cancel all background tasks."""
        for task in self._updater_tasks.values():
            task.cancel()

    # -------------------------------------------------------------------------
    # Task Management
    # -------------------------------------------------------------------------

    def _task_callback_check(self, result):
        """Handle task completion and restart if needed."""
        if not result.done():
            return
        if result.cancelled():
            LOG.info("Task %s was cancelled", str(result))
            return

        exception = result.exception()
        if not exception:
            return

        LOG.exception("Task raised an exception that was unhandled. Restarting.", exc_info=exception)

        lookup = {
            "club": self._club_updater,
            "player": self._player_updater,
            "maintenance": self._maintenance_poller,
        }

        for name, value in self._updater_tasks.items():
            if value != result:
                continue
            self._updater_tasks[name] = self.loop.create_task(lookup[name]())
            self._updater_tasks[name].add_done_callback(self._task_callback_check)

    @staticmethod
    def _safe_unlock(lock: asyncio.Lock):
        """Safely release a lock without raising if already released."""
        try:
            lock.release()
        except RuntimeError:
            pass

    # -------------------------------------------------------------------------
    # Polling Loops
    # -------------------------------------------------------------------------

    async def _maintenance_poller(self):
        """Poll for API maintenance status."""
        maintenance_start = None
        try:
            while self.loop.is_running():
                try:
                    # Use a well-known player tag to check API status
                    await asyncio.to_thread(self.get_player, "#2PP")
                    await asyncio.sleep(DEFAULT_SLEEP)
                except (Maintenance, ServiceException) as e:
                    # Check if it's a 503 (maintenance)
                    if isinstance(e, ServiceException) and getattr(e, 'status', None) != 503:
                        await asyncio.sleep(DEFAULT_SLEEP)
                        continue

                    if maintenance_start is None:
                        self._in_maintenance_event.clear()
                        maintenance_start = datetime.now(tz=timezone.utc).replace(tzinfo=None)
                        self.dispatch("maintenance_start")
                    await asyncio.sleep(15)
                except Exception:
                    await asyncio.sleep(DEFAULT_SLEEP)
                else:
                    if maintenance_start is not None:
                        self._in_maintenance_event.set()
                        self.dispatch("maintenance_completion", maintenance_start)
                        maintenance_start = None

        except asyncio.CancelledError:
            pass
        except Exception as exception:
            self.dispatch("event_error", exception)
            return await self._maintenance_poller()

    async def _club_updater(self):
        """Main club update loop."""
        try:
            while self.loop.is_running():
                await asyncio.sleep(DEFAULT_SLEEP)
                await self._in_maintenance_event.wait()

                self.dispatch("club_loop_start", self.club_loops_run)
                tasks = [
                    self.loop.create_task(self._run_club_update(index, tag))
                    for index, tag in enumerate(self._club_updates)
                ]
                if tasks:
                    await asyncio.gather(*tasks)
                self.dispatch("club_loop_finish", self.club_loops_run)
                self.club_loops_run += 1

        except asyncio.CancelledError:
            return
        except Exception as exception:
            self.dispatch("event_error", exception)
            for lock in (v for k, v in self._locks.items() if "club" in k):
                self._safe_unlock(lock)
            return await self._club_updater()

    async def _player_updater(self):
        """Main player update loop."""
        try:
            while self.loop.is_running():
                await asyncio.sleep(DEFAULT_SLEEP)
                await self._in_maintenance_event.wait()

                self.dispatch("player_loop_start", self.player_loops_run)
                tasks = [
                    self.loop.create_task(self._run_player_update(index, tag))
                    for index, tag in enumerate(self._player_updates)
                ]
                if tasks:
                    await asyncio.gather(*tasks)
                self.dispatch("player_loop_finish", self.player_loops_run)
                self.player_loops_run += 1

        except asyncio.CancelledError:
            return
        except Exception as exception:
            self.dispatch("event_error", exception)
            for lock in (v for k, v in self._locks.items() if "player" in k):
                self._safe_unlock(lock)
            return await self._player_updater()

    async def _run_club_update(self, index: int, club_tag: str):
        """Fetch club and run event listeners."""
        await asyncio.sleep(0.005 * index)  # Stagger requests

        key = f"club:{club_tag}"
        lock = self._locks.setdefault(key, asyncio.Lock())

        if lock.locked():
            return
        await lock.acquire()

        try:
            club = await asyncio.to_thread(self.get_club, club_tag)
        except (Maintenance, ServiceException):
            self._safe_unlock(lock)
            return
        except Exception as exception:
            self.dispatch("event_error", exception)
            self._safe_unlock(lock)
            return

        self.loop.call_later(
            max(DEFAULT_SLEEP, self.club_retry_interval),
            self._safe_unlock,
            lock
        )

        cached_club = self._get_cached_club(club_tag)
        self._update_club(club)

        if not cached_club:
            return

        for listener in self._listeners["club"]:
            if listener.tags and club_tag not in listener.tags:
                continue
            await listener(cached_club, club)

    async def _run_player_update(self, index: int, player_tag: str):
        """Fetch player and run event listeners."""
        await asyncio.sleep(0.005 * index)  # Stagger requests

        key = f"player:{player_tag}"
        lock = self._locks.setdefault(key, asyncio.Lock())

        if lock.locked():
            return
        await lock.acquire()

        try:
            player = await asyncio.to_thread(self.get_player, player_tag)
        except (Maintenance, ServiceException):
            self._safe_unlock(lock)
            return
        except Exception as exception:
            self.dispatch("event_error", exception)
            self._safe_unlock(lock)
            return

        self.loop.call_later(
            max(DEFAULT_SLEEP, self.player_retry_interval),
            self._safe_unlock,
            lock
        )

        cached_player = self._get_cached_player(player_tag)
        self._update_player(player)

        if cached_player is None:
            return

        for listener in self._listeners["player"]:
            if listener.tags and player_tag not in listener.tags:
                continue
            await listener(cached_player, player)
