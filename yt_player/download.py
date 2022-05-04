"""Downloads Youtube audios."""
import isort
import snoop
from colr import color
from pytube import YouTube
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def download():
    """
    Uses pytube to get information on the title
    and length of audio. Downloads the best audio
    mp4 stream available.
    """

    link = input(color(" (**) - Link? ", fore="#99C4C8"))
    yt = YouTube(link)
    print("\n")
    print(color(f" (**) - Title: {yt.title}", fore="#99C4C8"))
    print(color(f" (**) - Length of video: , {yt.length}, 'minutes'", fore="#99C4C8"))
    stream = yt.streams.get_audio_only()
    stream.download("music/")


if __name__ == "__main__":
    download()
