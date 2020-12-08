import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
import PyPDF2


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


def get_books_urls(url):
    urlsWithName = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.find_all("a", href=True):
        arr = a["href"].split(".")
        if arr[-1] == "pdf":
            urlsWithName.append(("http:" + a["href"], a.string))
    return urlsWithName


def get_books_and_create_folder(urls, target):
    if not os.path.isdir(target):
        os.makedirs(target)
    for url in urls:
        file = Path(target, url[1] + ".pdf")
        if not file.exists():
            response = requests.get(url[0])
            with open(Path(target, url[1] + ".pdf"), "wb+") as f:
                f.write(response.content)
        else:
            print("File already exists")


def save_text_from_pdf(name):
    file = Path(name + ".txt")
    if not file.exists():
        fileReader = PyPDF2.PdfFileReader(name)
        with open(Path(name + ".txt"), "a+") as f:
            for page in fileReader.pages:
                f.write(page.extractText())


def get_pfds_and_extract_to_text(url, folderName):
    urls = get_books_urls(url)
    get_books_and_create_folder(urls, folderName)
    p = Path(folderName)
    pdfFiles = list(p.glob('*.pdf'))
    for b_p in pdfFiles:
        save_text_from_pdf(os.path.join(folderName, b_p.name))
