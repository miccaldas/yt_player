"""Shows content of the 'music' folder and plays the users choice."""
import os
import subprocess

import isort
import questionary
import snoop
from colr import color
from questionary import Style
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def player():
    """
    Gets paths to all files and folders in 'music',
    puts them in a enumerated list for easy
    identification, asks the user the ids of the paths.
    If path is a directory, it'll play the full contents
    of the directory, if path is files, it'll play files.
    """

    custom_style_player = Style(
        [
            ("qmark", "fg:#FF5F00 bold"),
            ("question", "fg:#A2B38B bold"),
            ("answer", "fg:#F1DDBF bold"),
            ("instruction", "fg:#E4E9BE bold"),
            ("text", "fg:#F1DDBF bold"),
        ]
    )

    music_lst = []
    for root, dirs, files in os.walk("music"):
        for d in dirs:
            folder = os.path.relpath(os.path.join(root, d), "music")
            music_lst.append(folder)
        for f in files:
            song = os.path.relpath(os.path.join(root, f), "music")
            music_lst.append(song)
    enum_lst = list(enumerate(music_lst))
    for music in enum_lst:
        print(color(music, fore="#A2B38B"))
    print("\n")
    music_id = questionary.text("What are the ids of the music you want to hear?", qmark="(**)", style=custom_style_player).ask()
    id_lst = music_id.split(" ")
    int_lst = [int(i) for i in id_lst]
    for i in int_lst:
        for e in enum_lst:
            if i == e[0]:
                if os.path.isdir(e[1]):
                    cmd1 = "mpv --no-audio-display --play-dir '{e[1]}'"
                    subprocess.run(cmd1, cwd="music", shell=True)
                else:
                    cmd2 = f"mpv --no-audio-display '{e[1]}'"
                    subprocess.run(cmd2, cwd="music", shell=True)


if __name__ == "__main__":
    player()
