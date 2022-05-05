"""Module Docstring"""
import os

import isort
import questionary
import snoop
from colr import color
from questionary import Style
from snoop import pp
from youtubesearchpython import PlaylistsSearch


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def playlist(url, directory):
    """"""

    custom_style_playlist = Style(
        [
            ("qmark", "fg:#FF5F00 bold"),
            ("question", "fg:#A2B38B bold"),
            ("answer", "fg:#F1DDBF bold"),
            ("instruction", "fg:#E4E9BE bold"),
            ("text", "fg:#F1DDBF bold"),
        ]
    )

    music_folders = [i[0] for i in os.walk("music")]

    query = questionary.text(
        "What is your query?",
        qmark="(**)",
        style=custom_style_playlist,
    ).ask()
    fldr_name = query.replace(" ", "_")
    playlists = PlaylistsSearch(query, limit=30)
    print(playlists.result())

    """if directory is not None:
        if directory not in music_folders:
            band_folder = f"music/{directory}"
            os.mkdir(band_folder)
        else:
            band_folder = f"music/{directory}"""


if __name__ == "__main__":
    playlist()
