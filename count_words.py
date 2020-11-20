import re

import PyPDF2

book = open('book.pdf', 'rb')

fileReader = PyPDF2.PdfFileReader(book)

words = 0
i = 0

for page in fileReader.pages:
    page_text = page.extractText()
    words_on_page = re.findall('\w+', page_text)
    print(words_on_page)
    words += len(words_on_page)

print(words)

