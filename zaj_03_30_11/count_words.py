#!/usr/bin/python3

import os
from pathlib import Path

from pyspark import SparkContext

from zaj_01_20_11.webScrapper import get_books, save_text_from_pdf
from zaj_02_23_11.most_popular_words import most_popular_nouns, most_popular_words

folderName = "freud"
get_books("https://holybooks.com/sigmund-freud-the-complete-works/", folderName)

p = Path(folderName)
print(p)
pdfFiles = list(p.glob("*.pdf"))
for b_p in pdfFiles:
    save_text_from_pdf(os.path.join(folderName, b_p.name))

sc = SparkContext("local", "first app")
p = Path(folderName)
allTextFiles = list(p.glob("*.txt"))
files = []
for b_p in allTextFiles:
    files.append(sc.textFile(os.path.join(folderName, b_p.name)).cache())

for file in files:
    numXs = file.filter(lambda s: "x" in s).count()
    numYs = file.filter(lambda s: "y" in s).count()
    print(numXs, numYs)


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
