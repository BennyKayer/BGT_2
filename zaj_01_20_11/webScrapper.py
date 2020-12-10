import os
from pathlib import Path

import PyPDF2
import requests
from bs4 import BeautifulSoup


def get_books(url: str, target: str) -> None:
    """
    Save pdfs from given url

    Args:
        url (str): Where to get pdfs
        target (str): Where to save them
    """
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


def get_books_urls(url: str) -> list:
    """Returns named book urls

    Args:
        url (str): Url to books repo

    Returns:
        list: List of book urls
    """
    urlsWithName = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.find_all("a", href=True):
        arr = a["href"].split(".")
        if arr[-1] == "pdf":
            urlsWithName.append(("http:" + a["href"], a.string))
    return urlsWithName


def get_books_and_create_folder(urls: list, target: str) -> None:
    """Gets every pdf from urls in the list and saves them into local files

    Args:
        urls (list): List of urls to pdfs
        target (str): Local folder to save pdfs to
    """
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


def save_text_from_pdf(name: str) -> None:
    """Gets local pdf extracts its text then saves it to .txt

    Args:
        name (str): Local pdf path
    """
    file = Path(name + ".txt")
    if not file.exists():
        fileReader = PyPDF2.PdfFileReader(name)
        with open(Path(name + ".txt"), "a+") as f:
            for page in fileReader.pages:
                f.write(page.extractText())


def get_pfds_and_extract_to_text(url: str, folderName: str) -> None:
    """
    1. Gets individual urls
    2. Gets files and saves them into folder
    3. Extracts text and save it into .txts

    Args:
        url (str): Url to books repo
        folderName (str): Local folder to save pdfs to
    """
    urls = get_books_urls(url)
    get_books_and_create_folder(urls, folderName)
    p = Path(folderName)
    pdfFiles = list(p.glob("*.pdf"))
    for b_p in pdfFiles:
        save_text_from_pdf(os.path.join(folderName, b_p.name))
