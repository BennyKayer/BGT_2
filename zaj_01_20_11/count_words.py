import re

import PyPDF2


def count_words(name):
    fileReader = PyPDF2.PdfFileReader(name)

    words = 0
    for page in fileReader.pages:
        page_text = page.extractText()
        words_on_page = re.findall(r"\b[^\d\W]+\b", page_text)
        words += len(words_on_page)

    return words


def count_words_new(name):
    words = 0
    with open(name) as reader:
        text = reader.read()
        words_on_page = re.findall(r"\b[^\d\W]+\b", text)
        words += len(words_on_page)

    return words
