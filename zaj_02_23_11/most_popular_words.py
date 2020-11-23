
import PyPDF2


def words_frequency(name):
    book = open(name, 'rb')
    fileReader = PyPDF2.PdfFileReader(book)

    words = {}
    for page in fileReader.pages:
        page_text = page.extractText().split(' ')
        for word in page_text:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words


def most_popular_words(name):
    words = words_frequency(name)
    return sorted(words)[:10]


