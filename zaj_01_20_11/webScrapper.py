import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def get_books(url, target):
    if not os.path.isdir(target):
        os.makedirs(target)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.find_all("a", href=True):
        arr = a["href"].split(".")
        if arr[-1] == "pdf":
            response = requests.get("http:" + a["href"])
            with open(Path(target, a.string + ".pdf"), "wb+") as f:
                f.write(response.content)
