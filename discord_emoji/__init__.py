from .methods import to_unicode, to_discord, to_unicode_multi, to_discord_multi  # noqa
discord_to_unicode = to_unicode
unicode_to_discord = to_discord
discord_to_uni = to_unicode
unicode_to_dis = to_discord
to_uni = to_unicode
to_dis = to_discord

__all__ = (
    'to_unicode', 'to_discord', 'to_unicode_multi', 'to_discord_multi',
    'discord_to_unicode', 'unicode_to_discord', 'discord_to_uni', 'unicode_to_dis',
    'to_uni', 'to_dis'
)

__version__ = "1.4.2"
