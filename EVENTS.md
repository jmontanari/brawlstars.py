# Brawl Stars Events System

The Brawl Stars API library includes a powerful event system for real-time monitoring of players and clubs. This system uses decorator-based event registration with background polling for change detection.

## Quick Start

```python
import brawlstars

# Create an events client
client = brawlstars.EventsClient()
client.login_with_token("your_api_token")

# Register an event listener
@client.event
@brawlstars.ClubEvents.member_join()
async def on_member_join(member, club):
    print(f"{member.name} joined {club.name}!")

# Subscribe to tags
client.add_club_updates("#CLUB_TAG")

# Run the event loop
client.run_forever()
```

## Table of Contents

- [EventsClient](#eventsclient)
- [ClubEvents](#clubevents)
- [PlayerEvents](#playerevents)
- [ClientEvents](#clientevents)
- [Dynamic Events](#dynamic-events)
- [Tag Filtering](#tag-filtering)
- [Complete Example](#complete-example)

---

## EventsClient

The `EventsClient` extends the base `BrawlClient` with event polling capabilities.

### Initialization

```python
client = brawlstars.EventsClient(
    loop=None,                    # Optional: asyncio event loop
    club_retry_interval=0,        # Minimum seconds between club checks
    player_retry_interval=0,      # Minimum seconds between player checks
    club_cls=brawlstars.Club,     # Custom Club class (optional)
    player_cls=brawlstars.Player  # Custom Player class (optional)
)
```

### Authentication

```python
# Option 1: Email/password (auto-manages API keys)
client.login(username="email@example.com", password="your_password")

# Option 2: Direct token
client.login_with_token("your_api_token")
```

### Tag Subscription Methods

```python
# Add tags to monitor
client.add_club_updates("#TAG1", "#TAG2")
client.add_player_updates("#PLAYER1", "#PLAYER2")

# Remove tags
client.remove_club_updates("#TAG1")
client.remove_player_updates("#PLAYER1")

# With iterables
tags = ["#TAG1", "#TAG2", "#TAG3"]
client.add_club_updates(*tags)
```

### Lifecycle Methods

```python
# Blocking run
client.run_forever()

# Close and cancel tasks
client.close()
```

---

## ClubEvents

Events triggered by changes in club data.

### Predefined Events

#### `member_join`
Triggered when a new member joins the club.

```python
@client.event
@brawlstars.ClubEvents.member_join()
async def on_member_join(member, club):
    """
    Parameters
    ----------
    member : ClubMember
        The member who joined
    club : Club
        The club they joined
    """
    print(f"{member.name} joined {club.name}")
    print(f"Club now has {len(club.members)} members")
```

#### `member_leave`
Triggered when a member leaves the club.

```python
@client.event
@brawlstars.ClubEvents.member_leave()
async def on_member_leave(member, club):
    """
    Parameters
    ----------
    member : ClubMember
        The member who left (from cached data)
    club : Club
        The club they left
    """
    print(f"{member.name} left {club.name}")
```

### Dynamic Club Events

Any club attribute can be monitored:

```python
# Club name changed
@client.event
@brawlstars.ClubEvents.name()
async def on_name_change(old_club, new_club):
    print(f"Club renamed: {old_club.name} -> {new_club.name}")

# Club description changed
@client.event
@brawlstars.ClubEvents.description()
async def on_description_change(old_club, new_club):
    print(f"Description updated")

# Club trophies changed
@client.event
@brawlstars.ClubEvents.trophies()
async def on_trophies_change(old_club, new_club):
    diff = new_club.trophies - old_club.trophies
    print(f"Club trophies: {diff:+d}")

# Club type changed (open/inviteOnly/closed)
@client.event
@brawlstars.ClubEvents.type()
async def on_type_change(old_club, new_club):
    print(f"Club type: {old_club.type} -> {new_club.type}")

# Required trophies changed
@client.event
@brawlstars.ClubEvents.required_trophies()
async def on_required_trophies_change(old_club, new_club):
    print(f"Required trophies: {new_club.required_trophies}")
```

### Nested Member Events

Monitor changes to individual club members (prefix with `member_`):

```python
# Member trophies changed
@client.event
@brawlstars.ClubEvents.member_trophies()
async def on_member_trophies(old_member, new_member, club):
    """
    Parameters
    ----------
    old_member : ClubMember
        Previous member state
    new_member : ClubMember
        Current member state
    club : Club
        The club
    """
    diff = new_member.trophies - old_member.trophies
    print(f"{new_member.name} in {club.name}: {diff:+d} trophies")

# Member role changed (president/vicePresident/senior/member)
@client.event
@brawlstars.ClubEvents.member_role()
async def on_member_role(old_member, new_member, club):
    print(f"{new_member.name}: {old_member.role} -> {new_member.role}")

# Member name color changed
@client.event
@brawlstars.ClubEvents.member_name_color()
async def on_member_color(old_member, new_member, club):
    print(f"{new_member.name} changed their name color")
```

---

## PlayerEvents

Events triggered by changes in player data.

### Predefined Events

#### `brawler_unlock`
Triggered when a player unlocks a new brawler.

```python
@client.event
@brawlstars.PlayerEvents.brawler_unlock()
async def on_brawler_unlock(old_player, new_player, brawler):
    """
    Parameters
    ----------
    old_player : Player
        Previous player state
    new_player : Player
        Current player state
    brawler : BrawlerStat
        The newly unlocked brawler
    """
    print(f"{new_player.name} unlocked {brawler.name}!")
```

#### `brawler_upgrade`
Triggered when a player upgrades a brawler (power level, rank, gadgets, star powers).

```python
@client.event
@brawlstars.PlayerEvents.brawler_upgrade()
async def on_brawler_upgrade(old_player, new_player, old_brawler, new_brawler):
    """
    Parameters
    ----------
    old_player : Player
        Previous player state
    new_player : Player
        Current player state
    old_brawler : BrawlerStat
        Previous brawler state
    new_brawler : BrawlerStat
        Current brawler state
    """
    if old_brawler.power != new_brawler.power:
        print(f"{new_player.name} upgraded {new_brawler.name} to power {new_brawler.power}")
    if old_brawler.rank != new_brawler.rank:
        print(f"{new_player.name}'s {new_brawler.name} reached rank {new_brawler.rank}")
```

#### `club_join`
Triggered when a player joins a club.

```python
@client.event
@brawlstars.PlayerEvents.club_join()
async def on_club_join(old_player, new_player):
    """
    Parameters
    ----------
    old_player : Player
        Previous player state (club may be None or different)
    new_player : Player
        Current player state with new club
    """
    print(f"{new_player.name} joined {new_player.club.name}")
```

#### `club_leave`
Triggered when a player leaves a club.

```python
@client.event
@brawlstars.PlayerEvents.club_leave()
async def on_club_leave(old_player, new_player):
    """
    Parameters
    ----------
    old_player : Player
        Previous player state with old club
    new_player : Player
        Current player state (club may be None or different)
    """
    print(f"{old_player.name} left {old_player.club.name}")
```

### Dynamic Player Events

Any player attribute can be monitored:

```python
# Trophies changed
@client.event
@brawlstars.PlayerEvents.trophies()
async def on_trophies(old_player, new_player):
    diff = new_player.trophies - old_player.trophies
    print(f"{new_player.name}: {diff:+d} trophies (now {new_player.trophies})")

# Highest trophies changed
@client.event
@brawlstars.PlayerEvents.highest_trophies()
async def on_highest_trophies(old_player, new_player):
    print(f"{new_player.name} new PB: {new_player.highest_trophies}")

# Experience level changed
@client.event
@brawlstars.PlayerEvents.exp_level()
async def on_level_up(old_player, new_player):
    print(f"{new_player.name} reached level {new_player.exp_level}!")

# Solo victories changed
@client.event
@brawlstars.PlayerEvents.solo_victories()
async def on_solo_win(old_player, new_player):
    wins = new_player.solo_victories - old_player.solo_victories
    print(f"{new_player.name} got {wins} solo victory(s)")

# Duo victories changed
@client.event
@brawlstars.PlayerEvents.duo_victories()
async def on_duo_win(old_player, new_player):
    wins = new_player.duo_victories - old_player.duo_victories
    print(f"{new_player.name} got {wins} duo victory(s)")

# 3v3 victories changed
@client.event
@brawlstars.PlayerEvents.trio_victories()
async def on_3v3_win(old_player, new_player):
    wins = new_player.trio_victories - old_player.trio_victories
    print(f"{new_player.name} got {wins} 3v3 victory(s)")

# Player name changed
@client.event
@brawlstars.PlayerEvents.name()
async def on_name_change(old_player, new_player):
    print(f"Player renamed: {old_player.name} -> {new_player.name}")
```

---

## ClientEvents

System events triggered by the EventsClient itself.

```python
# API maintenance started
@client.event
@brawlstars.ClientEvents.maintenance_start()
async def on_maintenance_start():
    print("Brawl Stars API is under maintenance!")

# API maintenance ended
@client.event
@brawlstars.ClientEvents.maintenance_completion()
async def on_maintenance_end(time_started):
    """
    Parameters
    ----------
    time_started : datetime
        When maintenance started
    """
    from datetime import datetime, timezone
    duration = datetime.now(timezone.utc) - time_started
    print(f"Maintenance ended after {duration}")

# Unhandled error in event processing
@client.event
@brawlstars.ClientEvents.event_error()
async def on_error(exception):
    """
    Parameters
    ----------
    exception : Exception
        The exception that occurred
    """
    print(f"Event error: {exception}")

# Club update loop started
@client.event
@brawlstars.ClientEvents.club_loop_start()
async def on_club_loop_start(loop_count):
    print(f"Starting club update cycle #{loop_count}")

# Club update loop finished
@client.event
@brawlstars.ClientEvents.club_loop_finish()
async def on_club_loop_finish(loop_count):
    print(f"Finished club update cycle #{loop_count}")

# Player update loop started
@client.event
@brawlstars.ClientEvents.player_loop_start()
async def on_player_loop_start(loop_count):
    print(f"Starting player update cycle #{loop_count}")

# Player update loop finished
@client.event
@brawlstars.ClientEvents.player_loop_finish()
async def on_player_loop_finish(loop_count):
    print(f"Finished player update cycle #{loop_count}")
```

---

## Dynamic Events

The event system supports dynamic attribute monitoring for any model attribute. Simply use the attribute name as the event name:

```python
# Monitor any Club attribute
@brawlstars.ClubEvents.badge_id()      # Badge changed
@brawlstars.ClubEvents.member_count()  # Member count changed (use members for list)

# Monitor any Player attribute
@brawlstars.PlayerEvents.exp_points()          # XP points changed
@brawlstars.PlayerEvents.best_robo_rumble_time()  # Best Robo Rumble time changed
@brawlstars.PlayerEvents.best_time_as_big_brawler()  # Best Big Game time changed

# Monitor nested ClubMember attributes (prefix with member_)
@brawlstars.ClubEvents.member_icon()  # Member icon changed
```

---

## Tag Filtering

Filter events to only trigger for specific tags:

```python
# Only trigger for specific clubs
@client.event
@brawlstars.ClubEvents.member_join(tags=["#CLUB1", "#CLUB2"])
async def on_specific_club_join(member, club):
    print(f"{member.name} joined one of our tracked clubs!")

# Only trigger for specific players
@client.event
@brawlstars.PlayerEvents.trophies(tags="#MYPLAYER")
async def on_my_trophies(old_player, new_player):
    print(f"My trophies changed!")

# With retry interval (minimum seconds between checks)
@client.event
@brawlstars.ClubEvents.trophies(retry_interval=60)
async def on_club_trophies(old_club, new_club):
    print(f"Club trophies updated (checked max every 60s)")
```

---

## Complete Example

```python
import asyncio
import brawlstars

# Initialize client
client = brawlstars.EventsClient()
client.login_with_token("your_api_token")

# === Club Events ===

@client.event
@brawlstars.ClubEvents.member_join()
async def on_member_join(member, club):
    print(f"[JOIN] {member.name} joined {club.name} ({len(club.members)} members)")

@client.event
@brawlstars.ClubEvents.member_leave()
async def on_member_leave(member, club):
    print(f"[LEAVE] {member.name} left {club.name}")

@client.event
@brawlstars.ClubEvents.member_role()
async def on_role_change(old_member, new_member, club):
    print(f"[ROLE] {new_member.name}: {old_member.role} -> {new_member.role}")

@client.event
@brawlstars.ClubEvents.trophies()
async def on_club_trophies(old_club, new_club):
    diff = new_club.trophies - old_club.trophies
    print(f"[CLUB] {new_club.name} trophies: {diff:+d}")

# === Player Events ===

@client.event
@brawlstars.PlayerEvents.trophies()
async def on_player_trophies(old_player, new_player):
    diff = new_player.trophies - old_player.trophies
    emoji = "📈" if diff > 0 else "📉"
    print(f"{emoji} {new_player.name}: {diff:+d} trophies")

@client.event
@brawlstars.PlayerEvents.brawler_unlock()
async def on_brawler_unlock(old_player, new_player, brawler):
    print(f"🎉 {new_player.name} unlocked {brawler.name}!")

@client.event
@brawlstars.PlayerEvents.exp_level()
async def on_level_up(old_player, new_player):
    print(f"⬆️ {new_player.name} reached level {new_player.exp_level}!")

# === Client Events ===

@client.event
@brawlstars.ClientEvents.maintenance_start()
async def on_maintenance():
    print("⚠️ API maintenance started")

@client.event
@brawlstars.ClientEvents.event_error()
async def on_error(exception):
    print(f"❌ Error: {exception}")

# Subscribe to tags
client.add_club_updates("#2PP", "#YOURCLUB")
client.add_player_updates("#PLAYER1", "#PLAYER2")

# Run
print("Starting Brawl Stars event monitor...")
client.run_forever()
```

---

## Available Attributes Reference

### Club Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `tag` | str | Club tag |
| `name` | str | Club name |
| `description` | str | Club description |
| `trophies` | int | Total club trophies |
| `required_trophies` | int | Required trophies to join |
| `type` | str | Club type (open/inviteOnly/closed) |
| `badge_id` | int | Club badge ID |
| `members` | list | List of ClubMember objects |

### ClubMember Attributes (use `member_` prefix)
| Attribute | Type | Description |
|-----------|------|-------------|
| `tag` | str | Player tag |
| `name` | str | Player name |
| `trophies` | int | Player trophies |
| `role` | str | Role (president/vicePresident/senior/member) |
| `name_color` | str | Name color hex |

### Player Attributes
| Attribute | Type | Description |
|-----------|------|-------------|
| `tag` | str | Player tag |
| `name` | str | Player name |
| `name_color` | str | Name color hex |
| `trophies` | int | Current trophies |
| `highest_trophies` | int | Highest trophies achieved |
| `exp_level` | int | Experience level |
| `exp_points` | int | Experience points |
| `solo_victories` | int | Solo showdown wins |
| `duo_victories` | int | Duo showdown wins |
| `trio_victories` | int | 3v3 wins |
| `best_robo_rumble_time` | int | Best Robo Rumble time |
| `best_time_as_big_brawler` | int | Best Big Game time |
| `club` | PlayerClub | Current club info |
| `brawlers` | list | List of BrawlerStat objects |
