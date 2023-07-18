"""Downloads Youtube audios."""
import os

import questionary
import snoop
from colr import color
from pytube import YouTube
from questionary import Style
from snoop import pp

from search import search


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])

custom_style_download = Style(
    [
        ("qmark", "fg:#FF5F00 bold"),
        ("question", "fg:#A2B38B bold"),
        ("answer", "fg:#F1DDBF bold"),
        ("pointer", "fg:#F8CB2E bold"),
        ("highlighted", "fg:#FEFBE7 bold"),
        ("selected", "fg:#DAE5D0 bold"),
        ("instruction", "fg:#E4E9BE bold"),
        ("text", "fg:#F1DDBF bold"),
    ]
)


@snoop
def download():
    """
    Receives query and tuple with url, title and duration
    of each search result, asks the user to choose what
    results he wants to download by choosing the id of a
    enumerated search results list, checks for the tuple
    with the corresponding id, checks if there's already
    a folder in 'music' with the query's name, if yes, it
    downloads to it, if not, it creates a folder and
    downloads to it.
    """

    tups = search()
    music_folders = [i[0] for i in os.walk("music")]

    print("\n")
    for tup in enumerate(tups[1]):
        print(color(f" (**) - {tup}", fore="#A2B38B"))
    print("\n")

    entry_ids = questionary.text(
        "What ids do you want to choose?",
        qmark="(**)",
        style=custom_style_download,
        instruction="Choose the numbers of the entries you like",
    ).ask()

    lst_id = entry_ids.split(" ")
    int_id = [int(i) for i in lst_id]

    new_fldr = f"music/{tups[0]}"
    if new_fldr not in music_folders:
        os.mkdir(new_fldr)

    for id in int_id:
        for tup in enumerate(tups[1]):
            if id == tup[0]:
                YouTube(tup[1][0]).streams.get_audio_only().download(output_path=new_fldr)


if __name__ == "__main__":
    download()
