from __future__ import annotations

import sys
from titlecase import titlecase

try:
    import discord
except ImportError as err:
    err.msg = "alianator couldn't find Pycord or discord.py in your environment. Install one (and only one!) of " \
              "them, then try again."
    print(err, file=sys.stderr)
    exit(1)


def resolve(arg: discord.Permissions | int | str | tuple | list[str] | list[tuple], mode: bool = None) -> list[str]:
    """
    Resolves Discord permission names from their API flags to their user-facing aliases.

    :param arg: A discord.Permissions object, a integer, string tuple, list of strings, or list of tuples
    representing the permissions to resolve.

    :param mode: A boolean flag that determines which permissions will be resolved. If True, only granted
    permissions will be resolved. If False, only denied permissions will be resolved. If None, all permissions
    will be resolved. Defaults to None. If the function recieves a string or list of strings, all permissions will
    be resolved regardless of the value of this flag.

    :return: A list of strings containing the resolved permission aliases.
    """
    def resolver(names: list[str]) -> list[str]:
        resolutions = {
            "external_emojis": "Use External Emoji",
            "external_stickers": "Use External Stickers",
            "manage_emojis": "Manage Emojis and Stickers",
            "manage_guild": "Manage Server",
            "mention_everyone": "Mention \\@everyone, \\@here, and All Roles",
            "moderate_members": "Timeout Members",
            "send_tts_messages": "Send Text-to-Speech Messages",
            "start_embedded_activities": "Use Activities",
            "stream": "Video",
            "use_slash_commands": "Use Application Commands",
            "use_voice_activation": "Use Voice Activity",
        }

        return [resolutions.get(name) or titlecase(name.replace("_", " ")) for name in names]

    def validator(candidate: tuple | str) -> bool:
        if isinstance(candidate, tuple):
            return validator(candidate[0]) and isinstance(candidate[1], bool)
        elif isinstance(candidate, str):
            return candidate in discord.Permissions.VALID_FLAGS

    if not isinstance(mode, bool | None):
        raise TypeError("mode must be a boolean or None.")

    if isinstance(arg, list):
        if all(isinstance(x, str) for x in arg):
            if any(not validator(x) for x in arg):
                raise ValueError("List contains invalid permission flags")
            else:
                raws = arg

        elif all(isinstance(x, tuple) for x in arg):
            if any(not validator(x) for x in arg):
                raise TypeError("All permissions must be tuples of the format (str, bool) where str is a valid "
                                "permission flag.")
            else:
                raws = [x[0] for x in arg] if mode is None else [x[0] for x in arg if x[1] is mode]

        else:
            raise TypeError("If you pass in a list, it must be comprised of either exclusively strings or exclusively "
                            "tuples of the format (str, bool) where str is a valid permission flag.")

    elif isinstance(arg, str):
        if validator(arg):
            raws = [arg]
        else:
            raise ValueError(f"{arg} is not a valid permission flag.")

    elif isinstance(arg, tuple):
        if validator(arg):
            raws = [arg[0]] if mode is None else [arg[0]] if arg[1] is mode else []
        else:
            raise TypeError("If you pass in a tuple, it must be of the format (str, bool) where str is a valid "
                            "permission flag.")

    elif isinstance(arg, int):
        raws = [p[0] for p in discord.Permissions(arg)] if mode is None else [p[0] for p in discord.Permissions(arg)
                                                                              if p[1] is mode]

    elif isinstance(arg, discord.Permissions):
        raws = [p[0] for p in arg] if mode is None else [p[0] for p in arg if p[1] is mode]

    else:
        raise TypeError("Argument must be a discord.Permissions object, an integer, a string, a tuple, or a list.")

    return resolver(raws)
