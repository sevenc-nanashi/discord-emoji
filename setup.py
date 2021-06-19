import setuptools
from discord_emoji import __version__

with open("README.md", "r", encoding='utf-8') as f:
    long_desc = f.read()


def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()


setuptools.setup(
    name="discord-emoji",
    version=__version__,
    author="sevenc_nanashi",
    description="Converter of discord emoji and unicode emoji.",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url="https://github.com/sevenc-nanashi/discord-emoji",
    packages=['discord_emoji'],
    project_urls={
        "Bug Tracker": "https://github.com/sevenc-nanashi/discord-emoji/issues",
    },
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
