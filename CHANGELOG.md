# Changelog

All notable changes to this project will be documented in this file.

Breaking changes are marked with a 🚩.

## [4.0.0] - 2023-02-28 <a name="4-0-0"></a>

### Added

- alianator now keeps a proper changelog. You're reading it. Release notes from earlier versions have been ported over
  to this changelog.

### Changed

- The types to `alianator.resolve()` and `alianator.resolutions()` are no longer strictly enforced. As long as
  Pydantic can coerce your input to conform to the expected types, everything will be fine.

### Removed

- 🚩 `alianator.__version__` has been removed. Use `importlib.metadata` to query version information instead.

```py
from importlib import metadata

metadata.version("alianator")
```

## [3.3.0] - <a name="3-3-0">2023-02-28</a>

### Added

- `alianator.resolve()` now takes a optional, boolean, keyword-only, `escape_mentions` argument that, if `False`, will
  cause `mention_everyone` to resolve to `Mention @everyone, @here, and All Roles` instead
  of `Mention \@everyone, \@here, and All Roles`. The backslashes are necessary avoid accidental mass mentions in
  cases where alianator's output will ultimately be transformed into a Discord message, but if you don't want that,
  you can now turn it off. `escape_mentions` defaults to `True`.
- The new `alianator.resolutions()` function returns a dictionary mapping each existing permission flag to its
  resolution. It also accepts an optional `escape_mentions` argument, which works the same as it does
  in `alianator.resolve()`.

## [3.2.1] - <a name="3-2-1">2023-01-16</a>

No user-facing changes are introduced in this release.

## [3.2.0] - <a name="3-2-0">2023-01-13</a>

### Changed

- Arguments to `alianator.resolve()` are now validated by [Pydantic](https://docs.pydantic.dev). If you pass objects of
  unsupported types to `alianator.resolve()`, the resulting error message will probably be more helpful than it was
  previously.

## [3.1.0] - <a name="3-1-0">2022-12-26</a>

### Added

- alianator's now has a `diagnostic` module which prints some basic information about alianator and your development
  environment when run. You may be asked to provide the output of `python -m alianator.diagnostic` when opening issues.

### Changed

- `send_messages` now resolves to "Send Messages and Create Posts". (It previously resolved to "Send Messages".)
- `send_messages_in_threads` now resolves to "Send Messages in Threads and Posts". (It previously resolved to "Send
  Messages in Threads".)
- `manage_threads` now resolves to "Manage Threads and Posts". (It previously resolved to "Manage Threads".)
- `view_guild_insights` now resolves to "View Server Insights". (It previously resolved to "View Guild Insights".)

## [3.0.0] - <a name="3-0-0">2022-07-21</a>

### Removed

- 🚩 Support for [discord.py](https://github.com/Rapptz/discord.py) has been dropped,
  leaving [Pycord](https://github.com/Pycord-Development/pycord) as the only supported Discord API wrapper. alianator
  *might* still work with discord.py
  since Pycord is derivative of it and both libraries use the `discord` namespace, but I'm no longer making any promises
  to that end. Issues related to discord.py will be closed without comment.

## [2.0.0] - <a name="3-0-0">2022-04-16</a>

### Changed

- 🚩 `alianator.resolve()`'s `mode` parameter now defaults to True instead of None.
- alianator is now compatible with Python 3.8 and 3.9.

## [1.0.0] - <a name="1-0-0">2022-04-15</a>

This is the initial release of alianator.