from typing import List, overload

from .table import DISCORD_TO_UNICODE, UNICODE_TO_DISCORD


def discord_to_unicode(name: str) -> str:
    """Get unicode emoji from discord name.

    Parameters
    ----------
    name : str
        Name of the emoji to get.
        `:` will be ignored.

    Returns
    -------
    emoji : str
        The found emoji.

    Raises
    ------
    ValueError
        Raises when it couldn't find emoji.
    """
    real_name = name.strip(":")
    res = DISCORD_TO_UNICODE.get(real_name)
    if res is None:
        raise ValueError(f"Couldn't find emoji that named {real_name}.")
    else:
        return res


@overload
def unicode_to_discord(emoji: ..., get_all: True) -> List[str]:
    pass


@overload
def unicode_to_discord(emoji: ..., get_all: False) -> str:
    pass


def unicode_to_discord(emoji: str, get_all=False):
    """Get discord emoji name from unicode emoji.

    Parameters
    ----------
    emoji : str
        Emoji to get name.
    get_all : bool, optional
        [description], by default False

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
