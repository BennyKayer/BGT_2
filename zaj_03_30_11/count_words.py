#!/usr/bin/python3

from pyspark import SparkContext
import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup

import PyPDF2

def get_words(name):
    fileReader = PyPDF2.PdfFileReader(name)

    words = {}
    for page in fileReader.pages:
        page_text = page.extractText()
        words_on_page = re.findall(r'\b[^\d\W]+\b', page_text)
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
        words_on_page = re.findall(r'\b[^\d\W]+\b', page_text)
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
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        arr = a['href'].split('.')
        if arr[-1] == 'pdf':
            response = requests.get('http:' + a['href'])
            with open(Path(target, a.string + '.pdf'), 'wb+') as f:
                f.write(response.content)


get_books("https://holybooks.com/sigmund-freud-the-complete-works/", 'freud')
folderName = 'freud'
most_popular = {}
most_popular_ns = {}
p = Path('./freud')
for b_p in (list(p.glob('*.pdf'))):
    most_popular = most_popular_words(os.path.join(folderName, b_p.name))
    most_popular_ns = most_popular_nouns(os.path.join(folderName, b_p.name))

logFile = "loremIpsum.txt"
sc = SparkContext("local", "first app")
logData = sc.textFile(logFile).cache()
numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()
print("Lines with a: %i, lines with b: %i" % (numAs, numBs))
