import re

import PyPDF2


def count_words(name):
    book = open(name, 'rb')
    fileReader = PyPDF2.PdfFileReader(book)

    words = 0
    for page in fileReader.pages:
        page_text = page.extractText()
        words_on_page = re.findall('\w+', page_text)
        words += len(words_on_page)

    return words
