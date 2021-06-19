# discord_emoji
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
