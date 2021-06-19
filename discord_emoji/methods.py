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
def unicode_to_discord(emoji: ..., get_all: True, put_colons: ...) -> List[str]:
    pass


@overload
def unicode_to_discord(emoji: ..., get_all: False, put_colons: ...) -> Optional[str]:
    pass


def unicode_to_discord(emoji: str, get_all: bool = False, put_colons: bool = False):
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
            return None
        else:
            return []
    else:
        if put_colons:
            res = [f":{name}:" for name in res]
        if get_all:
            return res
        else:
            return res[0]
