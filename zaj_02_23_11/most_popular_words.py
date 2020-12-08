import re
from collections import Counter

import nltk


def words_frequency(name):
    words = {}
    with open(name) as reader:
        text = reader.read()
        words_in_text = re.findall(r"\b[^\d\W]+\b", text)
        for word in words_in_text:
            if word in words:
                words[word] += 1
            else:
                words[word] = 1
    return words


def is_noun(word):
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
