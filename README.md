# discord-emoji
[![PyPI](https://img.shields.io/pypi/v/discord-emoji)](https://pypi.org/project/discord-emoji) [![PyPI - Downloads](https://img.shields.io/badge/dynamic/json?label=downloads&query=%24.total_downloads&url=https%3A%2F%2Fapi.pepy.tech%2Fapi%2Fprojects%2Fdiscord-emoji)](https://pepy.tech/project/discord-emoji/)
This lib converts discord emoji and unicode emoji.

## Install
```
pip install discord-emoji
```

## Usage

```python
>>> import discord_emoji
>>> discord_emoji.discord_to_unicode("thinking")
'🤔'
>>> discord_emoji.discord_to_unicode(":thinking:")
'🤔'
>>> discord_emoji.unicode_to_discord("🤔")
'thinking'
>>> discord_emoji.unicode_to_discord("🤔", get_all=True)
['thinking', 'thinking_face']
```

## Licence

Please see [LICENSE](https://github.com/sevenc-nanashi/discord-emoji/blob/main/LICENSE).
