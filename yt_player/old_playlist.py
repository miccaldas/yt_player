"""Module Docstring"""
import os

import click
import isort
import snoop
from colr import color
from pytube import Playlist, YouTube
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@click.command()
@click.argument("url")
@click.option("-d", "--directory")
@snoop
def playlist(url, directory):
    """"""

    music_folders = [i[0] for i in os.walk("music")]

    if directory is not None:
        if directory not in music_folders:
            band_folder = f"music/{directory}"
            os.mkdir(band_folder)
        else:
            band_folder = f"music/{directory}"

    p = Playlist(url)
    for video in p.videos:
        video.streams.get_audio_only().download(band_folder)


if __name__ == "__main__":
    playlist()
