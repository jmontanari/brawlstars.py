# coding: utf-8

"""
    Brawl Stars API - Events

    Event system for the Brawl Stars API, providing decorator-based event
    registration and change detection for players and clubs.

    This module provides:
    - Event: Core event wrapper class
    - _ValidateEvent: Dynamic event creation helper
    - ClubEvents: Predefined club events (member_join, member_leave, etc.)
    - PlayerEvents: Predefined player events (brawler_unlock, club_join, etc.)
    - ClientEvents: Client/misc events (maintenance, errors, etc.)

    Example usage:
        import brawlstars

        @brawlstars.ClubEvents.member_join()
        async def on_member_join(member, club):
            print(f"{member.name} joined {club.name}")

        @brawlstars.PlayerEvents.trophies()
        async def on_trophy_change(old_player, new_player):
            diff = new_player.trophies - old_player.trophies
            print(f"{new_player.name}: {diff:+d} trophies")
"""

import asyncio
import logging
from collections.abc import Iterable
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from brawlstars.models.club import Club
    from brawlstars.models.player import Player

LOG = logging.getLogger(__name__)


class Event:
    """
    Object that is created for an event. This contains runner functions,
    tags and type.

    Attributes
    ----------
    runner : coroutine
        The async function that checks conditions and executes the callback.
    callback : coroutine
        The user's event listener function.
    tags : tuple
        Filter tags (e.g., specific club/player tags).
    type : str
        Event category: "club", "player", or "client".
    """

    __slots__ = ("runner", "callback", "tags", "type")

    def __init__(self, runner, callback, tags, type_):
        self.runner = runner
        self.callback = callback
        self.tags = tags
        self.type = type_

    def __call__(self, cached, current):
        return self.runner(cached, current, self.callback)

    def __eq__(self, other):
        return (
            isinstance(self, other.__class__)
            and self.runner == other.runner
            and self.callback == other.callback
        )

    @classmethod
    def from_decorator(cls, func, runner):
        """Helper classmethod to create an event from a decorated function."""
        return cls(runner, func, func.event_tags, func.event_type)


class _ValidateEvent:
    """Helper class to validate and register a function as an event.

    This class enables dynamic event creation through attribute access,
    allowing events like `@ClubEvents.trophies()` to work automatically
    for any model attribute.
    """

    def __init__(self, cls):
        self.cls = cls

    def __getattr__(self, item: str):
        try:
            return getattr(self.cls, item)
        except AttributeError:
            pass

        if self.cls.event_type == "client":
            return self.cls.__getattr__(self.cls, item)

        # Handle member_x events for nested club member attributes
        if "member_" in item and item != "member_count":
            item = item.replace("member_", "")
            nested = True
        else:
            nested = False

        return self._create_event(item.replace("_change", ""), nested)

    def _create_event(self, item, nested=False):
        def pred(cached, live) -> bool:
            return getattr(cached, item, None) != getattr(live, item, None)

        def actual(tags=None, custom_class=None, retry_interval=None):
            try:
                # Don't type check if it's nested
                custom_class and not nested and getattr(custom_class, item)
            except AttributeError:
                raise RuntimeError(f"custom_class does not have expected attribute {item}")

            def decorator(func):
                if nested:
                    wrap = _ValidateEvent.wrap_club_member_pred
                else:
                    wrap = _ValidateEvent.wrap_pred
                return _ValidateEvent.register_event(
                    func, wrap(pred), tags, custom_class, retry_interval, self.cls.event_type, item
                )

            return decorator

        return actual

    @staticmethod
    def shortcut_register(wrapped, tags, custom_class, retry_interval, event_type):
        """Fast route of registering an event for custom events that are manually defined."""

        def decorator(func):
            return _ValidateEvent.register_event(func, wrapped, tags, custom_class, retry_interval, event_type)

        return decorator

    @staticmethod
    def wrap_pred(pred):
        """Wraps a predicate in a coroutine that awaits the callback if the predicate is True."""

        async def wrapped(cached, live, callback):
            if pred(cached, live):
                await callback(cached, live)

        return wrapped

    @staticmethod
    def wrap_club_member_pred(pred):
        """Wraps a predicate for a club member (nested) attribute, and calls the callback."""

        async def wrapped(cached_club: "Club", club: "Club", callback):
            for member in club.members or []:
                cached_member = next(
                    (m for m in (cached_club.members or []) if m.tag == member.tag),
                    None
                )
                if cached_member is not None and pred(cached_member, member):
                    await callback(cached_member, member, club)

        return wrapped

    @staticmethod
    def register_event(func, runner, tags=None, cls=None, retry_interval=None, event_type="", event_name=""):
        """Validates the types of all arguments and adds these as attributes to the function."""
        if getattr(func, "is_event_listener", False) and func.event_type != event_type:
            raise RuntimeError("maximum of one event type per callback function.")

        if not asyncio.iscoroutinefunction(func):
            raise TypeError("callback function must be of type coroutine.")

        if not tags:
            tags = ()
        elif isinstance(tags, str):
            tags = (tags,)
        elif isinstance(tags, Iterable):
            tags = tuple(tags)
        else:
            raise TypeError(f"tags must be of type str, or iterable not {tags!r}")

        if retry_interval is not None and not isinstance(retry_interval, int):
            raise TypeError(f"retry_interval must be of type int not {retry_interval!r}")

        if not asyncio.iscoroutinefunction(runner):
            raise TypeError("runner function must be of type coroutine")

        func.event_type = event_type
        func.event_tags = tags
        func.is_event_listener = True
        func.event_cls = cls
        func.event_retry_interval = retry_interval
        func.event_name = event_name

        try:
            func.event_runners.append(runner)
        except AttributeError:
            func.event_runners = [runner]

        return func


@_ValidateEvent
class ClubEvents:
    """Predefined club events, or create your own with dynamic attribute access.

    Predefined Events
    -----------------
    member_join : Triggered when a member joins the club
        Callback signature: async def callback(member: ClubMember, club: Club)

    member_leave : Triggered when a member leaves the club
        Callback signature: async def callback(member: ClubMember, club: Club)

    Dynamic Events (via attribute access)
    -------------------------------------
    Any club attribute can be monitored by using it as an event name:
    - name : Club name changed
    - description : Club description changed
    - trophies : Club trophies changed
    - type : Club type changed (open/inviteOnly/closed)
    - required_trophies : Required trophies changed

    Nested member events (prefix with member_):
    - member_trophies : Member trophies changed
    - member_role : Member role changed
    - member_name_color : Member name color changed

    Example
    -------
    @brawlstars.ClubEvents.member_join()
    async def on_member_join(member, club):
        print(f"{member.name} joined {club.name}")

    @brawlstars.ClubEvents.trophies()
    async def on_club_trophies_change(old_club, new_club):
        print(f"Club trophies: {old_club.trophies} -> {new_club.trophies}")

    @brawlstars.ClubEvents.member_role()
    async def on_member_role_change(old_member, new_member, club):
        print(f"{new_member.name} role: {old_member.role} -> {new_member.role}")
    """

    event_type = "club"

    @classmethod
    def member_join(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a member has joined the club.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific club tags.
        custom_class : class, optional
            Custom Club class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(member: ClubMember, club: Club)
        """

        async def wrapped(cached_club, club, callback):
            current_tags = set(n.tag for n in (cached_club.members or []))
            if not current_tags:
                return
            members_joined = (n for n in (club.members or []) if n.tag not in current_tags)
            for member in members_joined:
                await callback(member, club)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, ClubEvents.event_type)

    @classmethod
    def member_leave(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a member has left the club.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific club tags.
        custom_class : class, optional
            Custom Club class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(member: ClubMember, club: Club)
        """

        async def wrapped(cached_club, club, callback):
            current_tags = set(n.tag for n in (club.members or []))
            if not current_tags:
                return
            members_left = (n for n in (cached_club.members or []) if n.tag not in current_tags)
            for member in members_left:
                await callback(member, club)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, ClubEvents.event_type)


@_ValidateEvent
class PlayerEvents:
    """Class that defines all valid player events.

    Predefined Events
    -----------------
    brawler_unlock : Triggered when a player unlocks a new brawler
        Callback signature: async def callback(old_player, new_player, brawler)

    brawler_upgrade : Triggered when a player upgrades a brawler
        Callback signature: async def callback(old_player, new_player, old_brawler, new_brawler)

    club_join : Triggered when a player joins a club
        Callback signature: async def callback(old_player, new_player)

    club_leave : Triggered when a player leaves a club
        Callback signature: async def callback(old_player, new_player)

    Dynamic Events (via attribute access)
    -------------------------------------
    Any player attribute can be monitored:
    - trophies : Player trophies changed
    - highest_trophies : Highest trophies changed
    - exp_level : Experience level changed
    - exp_points : Experience points changed
    - name : Player name changed
    - name_color : Name color changed
    - solo_victories : Solo victories changed
    - duo_victories : Duo victories changed
    - trio_victories : 3v3 victories changed

    Example
    -------
    @brawlstars.PlayerEvents.trophies()
    async def on_trophy_change(old_player, new_player):
        diff = new_player.trophies - old_player.trophies
        print(f"{new_player.name}: {diff:+d} trophies")

    @brawlstars.PlayerEvents.brawler_unlock()
    async def on_brawler_unlock(old_player, new_player, brawler):
        print(f"{new_player.name} unlocked {brawler.name}!")
    """

    event_type = "player"

    @classmethod
    def brawler_unlock(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a player has unlocked a new brawler.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific player tags.
        custom_class : class, optional
            Custom Player class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(old_player: Player, new_player: Player, brawler: BrawlerStat)
        """

        async def wrapped(cached_player, player, callback):
            cached_ids = set(b.id for b in (cached_player.brawlers or []))
            new_brawlers = (b for b in (player.brawlers or []) if b.id not in cached_ids)
            for brawler in new_brawlers:
                await callback(cached_player, player, brawler)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, PlayerEvents.event_type)

    @classmethod
    def brawler_upgrade(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a player has upgraded a brawler (power level, rank, gadgets, star powers).

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific player tags.
        custom_class : class, optional
            Custom Player class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(old_player: Player, new_player: Player, old_brawler: BrawlerStat, new_brawler: BrawlerStat)
        """

        async def wrapped(cached_player, player, callback):
            cached_brawlers = {b.id: b for b in (cached_player.brawlers or [])}
            for brawler in player.brawlers or []:
                cached_brawler = cached_brawlers.get(brawler.id)
                if cached_brawler and brawler != cached_brawler:
                    await callback(cached_player, player, cached_brawler, brawler)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, PlayerEvents.event_type)

    @classmethod
    def club_join(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a player has joined a club.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific player tags.
        custom_class : class, optional
            Custom Player class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(old_player: Player, new_player: Player)
        """

        async def wrapped(cached_player, player, callback):
            if cached_player.club is None and player.club is not None:
                await callback(cached_player, player)
            elif (
                cached_player.club is not None
                and player.club is not None
                and cached_player.club.tag != player.club.tag
            ):
                await callback(cached_player, player)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, PlayerEvents.event_type)

    @classmethod
    def club_leave(cls, tags=None, custom_class=None, retry_interval=None):
        """Event for when a player has left a club.

        Parameters
        ----------
        tags : str or iterable, optional
            Filter to only trigger for specific player tags.
        custom_class : class, optional
            Custom Player class to use for deserialization.
        retry_interval : int, optional
            Minimum seconds between checks for this event.

        Callback Signature
        ------------------
        async def callback(old_player: Player, new_player: Player)
        """

        async def wrapped(cached_player, player, callback):
            if cached_player.club is not None and player.club is None:
                await callback(cached_player, player)
            elif (
                cached_player.club is not None
                and player.club is not None
                and cached_player.club.tag != player.club.tag
            ):
                await callback(cached_player, player)

        return _ValidateEvent.shortcut_register(wrapped, tags, custom_class, retry_interval, PlayerEvents.event_type)


@_ValidateEvent
class ClientEvents:
    """Class that defines all valid client/misc events.

    These events are triggered by the EventsClient itself, not by changes
    in player or club data.

    Available Events
    ----------------
    maintenance_start : Triggered when API maintenance is detected
        Callback signature: async def callback()

    maintenance_completion : Triggered when maintenance ends
        Callback signature: async def callback(time_started: datetime)

    event_error : Triggered when an unhandled error occurs in event processing
        Callback signature: async def callback(exception: Exception)

    club_loop_start : Triggered at the start of each club update cycle
        Callback signature: async def callback(loop_count: int)

    club_loop_finish : Triggered at the end of each club update cycle
        Callback signature: async def callback(loop_count: int)

    player_loop_start : Triggered at the start of each player update cycle
        Callback signature: async def callback(loop_count: int)

    player_loop_finish : Triggered at the end of each player update cycle
        Callback signature: async def callback(loop_count: int)

    Example
    -------
    @brawlstars.ClientEvents.maintenance_start()
    async def on_maintenance():
        print("API is under maintenance!")

    @brawlstars.ClientEvents.event_error()
    async def on_error(exception):
        print(f"Error occurred: {exception}")
    """

    event_type = "client"

    def __getattr__(self, item):
        def wrapped():
            def deco(function):
                function.is_client_event = True
                function.event_name = item
                return function

            return deco

        return wrapped
