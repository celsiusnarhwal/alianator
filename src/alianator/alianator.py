from __future__ import annotations

from typing import Union, Optional

from multimethod import multimethod
from pydantic import validate_arguments
from titlecase import titlecase

__all__ = ["resolve", "resolutions"]

try:
    import discord
except ImportError as err:
    err.msg = "alianator couldn't find Pycord in your environment. Install it, then try again."
    raise err


class PermissionFlagMeta(type):
    def __new__(mcs, name, *args, **kwargs):
        return super().__new__(mcs, "discord.Permissions.VALID_FLAGS", *args, **kwargs)

    def __instancecheck__(self, instance):
        return instance in discord.Permissions.VALID_FLAGS


class PermissionFlag(metaclass=PermissionFlagMeta):
    pass


@validate_arguments(config=dict(arbitrary_types_allowed=True))
def resolve(
    arg: Union[
        discord.Permissions,
        int,
        PermissionFlag,
        tuple[PermissionFlag, bool],
        list[PermissionFlag],
        list[tuple[PermissionFlag, bool]],
    ],
    mode: Optional[bool] = True,
    *,
    escape_mentions: Optional[bool] = True,
) -> list[str]:
    """
    Resolve Discord permission names from their API flags to their user-facing aliases.

    Parameters
    ----------
    arg : Union[discord.Permissions, int, str, tuple[str, bool], list[str], list[tuple[str, bool]]]
        An object representing the permissions to resolve.
    mode : bool, optional, default: True
        A boolean flag that determines which permissions will be resolved. If True, only granted permissions will be
        resolved. If False, only denied permissions will be resolved. If None, all permissions will be resolved.
        If the function recieves a string or list of strings, all permissions will be resolved regardless of the value
        of this flag.
    escape_mentions : bool, optional, default: True
        Whether to escape mentions in the resolution for `mention_everyone`. If `mention_everyone` is not one of
        the permissions being resolved, this flag has no effect.

    Returns
    -------
    list[str]
        A list of resolved permissions.
    """

    def resolver(names: list[str]) -> list[str]:
        # manually define resolutions that can't be accomplished by simple character substitution
        resolutions_ = {
            "send_messages": "Send Messages and Create Posts",
            "send_messages_in_threads": "Send Messages in Threads and Posts",
            "external_emojis": "Use External Emoji",
            "external_stickers": "Use External Stickers",
            "manage_emojis": "Manage Emojis and Stickers",
            "manage_threads": "Manage Threads and Posts",
            "mention_everyone": "Mention \\@everyone, \\@here, and All Roles",
            "moderate_members": "Timeout Members",
            "send_tts_messages": "Send Text-to-Speech Messages",
            "start_embedded_activities": "Use Activities",
            "stream": "Video",
            "use_slash_commands": "Use Application Commands",
            "use_voice_activation": "Use Voice Activity",
        }

        if not escape_mentions:
            resolutions_["mention_everyone"] = resolutions_["mention_everyone"].replace(
                "\\", ""
            )

        return [
            resolutions_.get(name)
            or titlecase(name.replace("_", " ").replace("guild", "server"))
            for name in names
        ]

    @multimethod
    def solution(permissions: Union[discord.Permissions, list[tuple[str, bool]]]):
        return resolver(
            [perm for perm, status in permissions if mode in [status, None]]
        )

    @multimethod
    def solution(permissions: list[str]):
        return resolver(permissions)

    @multimethod
    def solution(permissions: Union[str, tuple[str, bool]]):
        return solution([permissions])

    @multimethod
    def solution(permissions: int):
        return solution(discord.Permissions(permissions))

    return solution(arg)


@validate_arguments
def resolutions(*, escape_mentions: Optional[bool] = True):
    """
    Return a dictionary of all available permission resolutions.

    Parameters
    ----------
    escape_mentions : bool, optional, default: True
        Whether to escape mentions in the resolution for `mention_everyone`.

    Returns
    -------
    dict[str, str]
        A dictionary of all possible permission resolutions.
    """

    return {
        name: resolve(name, escape_mentions=escape_mentions)[0]
        for name in discord.Permissions.VALID_FLAGS
    }
