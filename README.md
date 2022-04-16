# alianator
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/alianator?color=03cb98&logo=python&logoColor=03cb98&style=for-the-badge) ![PyPI](https://img.shields.io/pypi/v/alianator?color=03cb98&logo=pypi&logoColor=03cb98&style=for-the-badge) ![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/alianator?color=03cb98&label=latest%20release&logo=github&logoColor=03cb98&sort=semver&style=for-the-badge)

alianator is a tool that helps [Pycord](https://github.com/Pycord-Development/pycord) and
[discord.py](https://github.com/Rapptz/discord.py) users easily resolve user-facing aliases for Discord permission
flags.

## Installation

```bash
$ pip install alianator
```

alianator doesn't include either Pycord or discord.py as a dependency; instead, it allows you to use whichever of the 
two libraries you prefer. alianator **does not and will not** support other Discord API wrappers, such as
[Nextcord](https://github.com/nextcord/nextcord), [Hikari](https://github.com/hikari-py/hikari), or
[disnake](https://github.com/DisnakeDev/disnake).

## Usage

alianator can resolve aliases from `discord.Permissions` objects, integers, strings, tuples, lists of strings, and lists
of tuples.

```python
import alianator

alianator.resolve(arg, mode=mode)
```

The optional `mode` flag can be used to specify which permission should be resolved. If `mode` is `True`, only granted
permissions will be resolved; if `mode` is `False`, only denied permissions will be resolved; if `mode` is `None`, all
permissions will be resolved. If `mode` is not explicitly specified, it will default to `None`.

```python
import alianator
import discord

# Resolving from a discord.Permissions object
perms = discord.Permissions.general()
aliases = alianator.resolve(perms, mode=True)
print(aliases)
# ['Manage Channels', 'Manage Server', 'View Audit Log', 'Read Messages', 'View Guild Insights', 'Manage Roles', 'Manage Webhooks', 'Manage Emojis and Stickers']


# Resolving from an integer
perms = 3072
aliases = alianator.resolve(perms, mode=True)
print(aliases)
# ['Read Messages', 'Send Messages']


# Resolving from a string
perms = "send_tts_messages"
aliases = alianator.resolve(perms, mode=True)
print(aliases)
# ['Send Text-To-Speech Messages']


# Resolving from a tuple
perms = ("moderate_members", True)
aliases = alianator.resolve(perms, mode=True)
print(aliases)
# ['Timeout Members']


# Resolving from a list of strings
perms = ["manage_guild", "manage_emojis"]
aliases = alianator.resolve(perms, mode=True)
print(aliases)
# ['Manage Server', 'Manage Emojis and Stickers']


# Resolving from a list of tuples
perms = [("use_slash_commands", True), ("use_voice_activation", True)]
aliases = alianator.resolve(perms, mode=True)
print(aliases)
# ['Use Application Commands', 'Use Voice Activity']
```

That's about all there is to it. alianator does one thing and does it well.

## License

alianator is released under the [MIT License](https://github.com/celsiusnarhwal/alianator/blob/master/LICENSE.md).
