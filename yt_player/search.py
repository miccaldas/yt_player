"""Module Docstring"""
import re
import urllib.request

import isort
import snoop
from colr import color
from snoop import pp
from youtube_search import YoutubeSearch


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def search():
    """"""

    search = input(color("(**) - What Are You Looking For? ", fore="#E8C07D"))
    search = search.replace(" ", "+")
    yt_search = f"https://www.youtube.com/results?search_query={search}"
    html = urllib.request.urlopen(yt_search)
    vhtml = html.read().decode()
    with open("html.txt", "w") as f:
        f.write(vhtml)

    """v_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())

    final_urls = []
    for v in v_ids:
        fv = f"https://www.youtube.com/watch?v={v}"
        final_urls.append(fv)
    for f in final_urls:
        print(f)"""


if __name__ == "__main__":
    search()
