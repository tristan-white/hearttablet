# import the main window object (mw) from aqt
from aqt import mw
# import the "show info" tool from utils.py
from aqt.utils import showInfo, qconnect
# import all of the Qt GUI library
from aqt.qt import *

import requests
import json

# We're going to add a menu item below. First we want to create a function to
# be called when the menu item is activated.

def testFunction() -> None:
    # get the number of cards in the current collection, which is stored in
    # the main window
    # cardCount = mw.col.card_count()
    # show a message box
    # showInfo("Card count: %d" % cardCount)

    # query ESV API for a verse
    verse = "John 3:16"
    url = f"https://api.esv.org/v3/passage/text/"
    headers = {
        "Authorization": "Token "
    }
    params = {
        "q": verse,
        "include-passage-references": "false",
        "include-verse-numbers": "false",
        "include-first-verse-numbers": "false",
        "include-footnotes": "false",
        "include-footnote-body": "false",
        "include-headings": "false",
        "include-short-copyright": "false",
        "indent-paragraphs": "1",
        "indent-using": "tab",
        "indent-poetry": "false"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        showInfo(json.dumps(data, indent=2))
    else:
        showInfo(f"Error fetching passage: {response.status_code}")

# create a new menu item, "test"
action = QAction("test", mw)
# # set it to call testFunction when it's clicked
qconnect(action.triggered, testFunction)
# # and add it to the tools menu
mw.form.menuTools.addAction(action)
