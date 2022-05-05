"""Searches Youtube for a query."""
import isort
import questionary
import snoop
from questionary import Style
from snoop import pp
from youtubesearchpython import Search


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def search():
    """
    Asks user for a query, prepares the query string
    to be a folder name, asks how many results does
    the user wants. By default it searches 30 results.
    From these results it takes the values of video id,
    builds a youtube url with it, and the title and
    duration values in the search result. Returns them.
    """

    custom_style_search = Style(
        [
            ("qmark", "fg:#FF5F00 bold"),
            ("question", "fg:#A2B38B bold"),
            ("answer", "fg:#F1DDBF bold"),
            ("instruction", "fg:#E4E9BE bold"),
            ("text", "fg:#F1DDBF bold"),
        ]
    )

    query = questionary.text(
        "What is your query?",
        qmark="(**)",
        style=custom_style_search,
        instruction="Choose what you'll be searching for.",
    ).ask()

    lmt = questionary.text(
        "How many results do you want?",
        qmark="(**)",
        style=custom_style_search,
        default="30",
        instruction="Choose how many search results you'll get.",
    ).ask()

    fldr_name = query.replace(" ", "_")
    number_of_searches = int(lmt)
    srch = Search(query, limit=number_of_searches)
    tup_lst = []
    results = srch.result()
    for i in range(len(results["result"])):
        ident = results["result"][i]["id"]
        url = f"https://www.youtube.com/watch?v={ident}"
        tit = results["result"][i]["title"]
        try:
            dur = results["result"][i]["duration"]
        except KeyError as e:
            print("Error is", e)
        tup = (url, tit, dur)
        tup_lst.append(tup)

    return fldr_name, tup_lst


if __name__ == "__main__":
    search()
