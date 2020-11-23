import re
from collections import Counter

from nltk.corpus import wordnet as wn
import PyPDF2


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


def is_noun(word):
    try:
        partOfSpeech = wn.synsets(word)[0].pos()
        if isinstance(partOfSpeech, list):
            if 'n' in partOfSpeech:
                return True
        if isinstance(partOfSpeech, str):
            if 'n' == partOfSpeech:
                return True
    except IndexError:
        return False
    return False


def most_popular_nouns(name):
    words = words_frequency(name)
    copied = dict(words)
    for key in words:
        if not is_noun(key):
            del copied[key]
    k = Counter(copied)
    return k.most_common(10)


def most_popular_words(name):
    words = words_frequency(name)
    k = Counter(words)
    return k.most_common(10)

