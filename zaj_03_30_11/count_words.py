#!/usr/bin/python3
import os
import re
from pathlib import Path
from collections import Counter

import nltk
import PyPDF2
import requests
from bs4 import BeautifulSoup
from pyspark import SparkContext


def is_noun(word):
    nltk.download("averaged_perceptron_tagger")
    partOfSpeech = nltk.pos_tag([word])
    if "NN" == partOfSpeech[0][1]:
        return True
    return False


def most_popular_nouns(name):
    words = words_frequency(name)
    copied = dict(words)
    del copied["s"]
    for key in words:
        if not is_noun(key):
            del copied[key]
    k = Counter(copied)
    return k.most_common(3)


def most_popular_words(name):
    words = words_frequency(name)
    k = Counter(words)
    return k.most_common(10)


def get_words(name):
    fileReader = PyPDF2.PdfFileReader(name)

    words = {}
    for page in fileReader.pages:
        page_text = page.extractText()
        words_on_page = re.findall(r"\b[^\d\W]+\b", page_text)
        for word in words_on_page:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words


def words_frequency(name):
    fileReader = PyPDF2.PdfFileReader(name)

    words = {}
    for page in fileReader.pages:
        page_text = page.extractText()
        words_on_page = re.findall(r"\b[^\d\W]+\b", page_text)
        for word in words_on_page:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words


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


get_books("https://holybooks.com/sigmund-freud-the-complete-works/", "freud")
folderName = "freud"
most_popular = {}
most_popular_ns = {}
p = Path("./freud")
for b_p in list(p.glob("*.pdf")):
    most_popular = most_popular_words(os.path.join(folderName, b_p.name))
    most_popular_ns = most_popular_nouns(os.path.join(folderName, b_p.name))

logFile = "loremIpsum.txt"
sc = SparkContext("local", "first app")
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: "a" in s).count()
numBs = logData.filter(lambda s: "b" in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
