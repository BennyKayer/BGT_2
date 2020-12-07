#!/usr/bin/python3

from pyspark import SparkContext, SparkFiles

import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup

import PyPDF2
import re
from collections import Counter


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


def save_text_from_pdf(name):
    fileReader = PyPDF2.PdfFileReader(name)
    with open(Path(name + ".txt"), "a+") as f:
        for page in fileReader.pages:
            f.write(page.extractText())


def words_frequency(page_text):
    words = {}
    words_list = re.findall(r"\b[^\d\W]+\b", page_text)
    print(page_text)
    for word in words_list:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


def most_popular_words(name):
    words = words_frequency(name)
    print(words)
    k = Counter(words)
    return k.most_common(10)


folderName = 'freud'
get_books("https://holybooks.com/sigmund-freud-the-complete-works/", folderName)

p = Path(folderName)
print(p)
pdfFiles = list(p.glob('*.pdf'))
for b_p in pdfFiles:
    save_text_from_pdf(os.path.join(folderName, b_p.name))

sc = SparkContext("local", "first app")
p = Path(folderName)
allTextFiles = list(p.glob('*.txt'))
files = []
for b_p in allTextFiles:
    files.append(sc.textFile(os.path.join(folderName, b_p.name)).cache())

for file in files:
    numXs = file.filter(lambda s: 'x' in s).count()
    numYs = file.filter(lambda s: 'y' in s).count()
    print(numXs, numYs)
# file.
# mostPopular = most_popular_words(file)
# print(mostPopular)
