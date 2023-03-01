# alianator

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/alianator?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/alianator)
[![PyPI](https://img.shields.io/pypi/v/alianator?logo=pypi&color=green&logoColor=white&style=for-the-badge)](https://pypi.org/project/alianator)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/alianator?logo=github&color=orange&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/alianator/releases)
[![PyPI - License](https://img.shields.io/pypi/l/alianator?color=03cb98&style=for-the-badge)](https://github.com/celsiusnarhwal/alianator/blob/master/LICENSE)
[![Black](https://aegis.celsiusnarhwal.dev/badge/black?style=for-the-badge)](https://github.com/psf/black)

alianator is a Discord permission name resolver for [Pycord](https://github.com/Pycord-Development/pycord). 
It takes Discord's API permission flags (e.g. `manage_guild`) and resolves them to their user-facing aliases (e.g. `Manage Server`).

## Installation

```bash
$ pip install alianator
```

[Pycord](https://github.com/Pycord-Development/pycord) is not included as a dependency of alianator, but nonetheless must 
be installed for it to work. If alianator is unable to import the `discord` namespace, it will raise an `ImportError`.

## Usage

alianator can resolve aliases from `discord.Permissions` objects, integers, strings, tuples, lists of strings, and lists
of tuples.

```python
import alianator

alianator.resolve(arg, mode=mode)
```

The optional `mode` flag can be used to specify which permissions should be resolved. If `mode` is `True`, only granted
permissions will be resolved; if `mode` is `False`, only denied permissions will be resolved; if `mode` is `None`, all
permissions will be resolved. If `mode` is not explicitly specified, it will default to `True`.

```python
import alianator
import discord

# Resolving from a discord.Permissions object
perms = discord.Permissions.general()
aliases = alianator.resolve(perms)
print(aliases)
# ['Manage Channels', 'Manage Server', 'View Audit Log', 'Read Messages', 'View Server Insights', 'Manage Roles', 'Manage Webhooks', 'Manage Emojis and Stickers']


# Resolving from an integer
perms = 3072
aliases = alianator.resolve(perms)
print(aliases)
# ['View Channel', 'Send Messages and Create Posts']


# Resolving from a string
perms = "send_tts_messages"
aliases = alianator.resolve(perms)
print(aliases)
# ['Send Text-To-Speech Messages']


# Resolving from a tuple
perms = ("moderate_members", True)
aliases = alianator.resolve(perms)
print(aliases)
# ['Timeout Members']


# Resolving from a list of strings
perms = ["manage_guild", "manage_emojis"]
aliases = alianator.resolve(perms)
print(aliases)
# ['Manage Server', 'Manage Emojis and Stickers']


# Resolving from a list of tuples
perms = [("use_slash_commands", True), ("use_voice_activation", True)]
aliases = alianator.resolve(perms)
print(aliases)
# ['Use Application Commands', 'Use Voice Activity']
```

That's about all there is to it. alianator does one thing and does it well.

## License

alianator is released under the [MIT License](https://github.com/celsiusnarhwal/alianator/blob/master/LICENSE.md).
