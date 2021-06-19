from typing import List, Optional, overload

from .table import DISCORD_TO_UNICODE, UNICODE_TO_DISCORD


def discord_to_unicode(name: str) -> Optional[str]:
    """Get unicode emoji from discord name.
    Returns None if couldn't find emoji.

    Parameters
    ----------
    name : str
        Name of the emoji to get.
        `:` will be ignored.

    Returns
    -------
    emoji : str
        The found emoji.
    """
    real_name = name.strip(":")
    res = DISCORD_TO_UNICODE.get(real_name)
    if res is None:
        raise ValueError(f"Couldn't find emoji that named {real_name}.")
    else:
        return res


@overload
def unicode_to_discord(emoji: ..., get_all: True) -> Optional[List[str]]:
    pass


@overload
def unicode_to_discord(emoji: ..., get_all: False) -> Optional[str]:
    pass


def unicode_to_discord(emoji: str, get_all=False):
    """Get discord emoji name from unicode emoji.
    Returns None if couldn't find emoji.

    Parameters
    ----------
    emoji : str
        Emoji to get name.
    get_all : bool, optional
        Whether get all emoji names, by default False

    Returns
    -------
    name : Union[str, List[str]]
        Name of the found emoji.
        If get_all is True, it will return list.

    Raises
    ------
    ValueError
        Raises when it isn't emoji, or it isn't supported.
    """
    res = UNICODE_TO_DISCORD.get(emoji)
    if res is None:
        raise ValueError(f"{emoji} is not emoji, or not supported.")
    else:
        if get_all:
            return res
        else:
            return res[0]
