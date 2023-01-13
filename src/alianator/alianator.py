from __future__ import annotations

from typing import Union, Optional

from multimethod import multimethod
from pydantic import StrictInt, StrictBool, validate_arguments
from titlecase import titlecase

try:
    import discord
except ImportError as err:
    err.msg = "alianator couldn't find Pycord in your environment. Install it, then try again."
    raise err


class _PermissionFlagMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        name = namespace.get("__name__", "discord.Permissions.VALID_FLAGS")
        return super().__new__(mcs, name, bases, namespace, **kwargs)

    def __instancecheck__(self, instance):
        return instance in discord.Permissions.VALID_FLAGS


class _PermissionFlag(metaclass=_PermissionFlagMeta):
    pass


@validate_arguments(config=dict(arbitrary_types_allowed=True))
def resolve(
    arg: Union[
        discord.Permissions,
        StrictInt,
        _PermissionFlag,
        tuple[_PermissionFlag, StrictBool],
        list[_PermissionFlag],
        list[tuple[_PermissionFlag, StrictBool]],
    ],
    mode: Optional[StrictBool] = True,
) -> list[str]:
    """
    Resolves Discord permission names from their API flags to their user-facing aliases.

    Parameters
    ----------
    arg : Union[discord.Permissions, int, str, tuple[str, bool], list[str], list[tuple[str, bool]]]
        An object representing the permissions to resolve.
    mode : bool, optional
        A boolean flag that determines which permissions will be resolved. If True, only granted permissions will be
        resolved. If False, only denied permissions will be resolved. If None, all permissions will be resolved.
        Defaults to True. If the function recieves a string or list of strings, all permissions will be resolved
        regardless of the value of this flag.

    Returns
    -------
    list[str]
        A list of resolved permissions.
    """

    def resolver(names: list[str]) -> list[str]:
        # manually define resolutions that can't be accomplished by simple character substitution
        resolutions = {
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

        return [
            resolutions.get(name)
            or titlecase(name.replace("_", " ").replace("guild", "server"))
            for name in names
        ]

    @multimethod
    def _resolve(permissions: Union[discord.Permissions, list[tuple[str, bool]]]):
        return resolver(
            [perm for perm, status in permissions if mode in [status, None]]
        )

    @multimethod
    def _resolve(permissions: list[str]):
        return resolver(permissions)

    @multimethod
    def _resolve(permissions: tuple[str, bool]):
        return resolver([permissions[0]]) if mode in [permissions[1], None] else []

    @multimethod
    def _resolve(permissions: str):
        return resolver([permissions])

    @multimethod
    def _resolve(permissions: int):
        return resolver(
            [
                perm
                for perm, status in discord.Permissions(permissions)
                if mode in [status, None]
            ]
        )

    return _resolve(arg)
