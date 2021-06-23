from typing import List, Optional, overload

from .table import DISCORD_TO_UNICODE, UNICODE_TO_DISCORD


def to_unicode(name: str) -> Optional[str]:
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
    return res


@overload
def to_discord(emoji: ..., get_all: True, put_colons: ...) -> List[str]:
    pass


@overload
def to_discord(emoji: ..., get_all: False, put_colons: ...) -> Optional[str]:
    pass


def to_discord(emoji: str, get_all: bool = False, put_colons: bool = False):
    """Get discord emoji name from unicode emoji.
    Returns None or empty list if couldn't find emoji.

    Parameters
    ----------
    emoji : str
        Emoji to get name.
    get_all : bool, optional
        Whether get all emoji names, by default False
    put_colons : bool, optional
        Whether put colons to names.

    Returns
    -------
    name : Union[str, List[str]]
        Name of the found emoji.
        If get_all is True, it will return list.
    """
    res = UNICODE_TO_DISCORD.get(emoji)
    if res is None:
        if get_all:
            return []
        else:
            return None
    else:
        if put_colons:
            res = [f":{name}:" for name in res]
        if get_all:
            return res
        else:
            return res[0]


def to_discord_multi(base: str) -> str:
    """Replaces unicode emoji to discord name with colons.

    Parameters
    ----------
    base : str
        String to convert.

    Returns
    -------
    str
        Converted string.
    """
    res = base
    for unicode_char, discord_name in UNICODE_TO_DISCORD.items():
        res = res.replace(unicode_char, f":{discord_name[0]}:")

    return res


def to_unicode_multi(base: str) -> str:
    """Replaces discord name with colons to unicode emoji.

    Parameters
    ----------
    base : str
        String to convert.

    Returns
    -------
    str
        Converted string.
    """
    res = base
    for discord_name, unicode_char in DISCORD_TO_UNICODE.items():
        res = res.replace(f":{discord_name}:", unicode_char)

    return res
