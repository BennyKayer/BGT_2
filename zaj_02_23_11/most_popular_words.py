import re
from collections import Counter

import nltk


def words_frequency(name: str) -> dict:
    """Creates words frequency dictionary

    Args:
        name (str): Local path

    Returns:
        dict: Words frequency dictionary
    """
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


def is_noun(word: str) -> bool:
    """Checks whether word is a noun using nltk

    Args:
        word (str): Word to check

    Returns:
        bool: True if word is a noun False otherwise
    """
    partOfSpeech = nltk.pos_tag([word])
    if "NN" == partOfSpeech[0][1]:
        return True
    return False


def most_popular_nouns(name: str) -> list:
    """Copies dict with all words, deletes ones that are not nouns then returns 3 most common ones

    Args:
        name (str): Path to local pdf

    Returns:
        list: 3 nouns with most occurences
    """
    words = words_frequency(name)
    copied = dict(words)
    del copied["s"]
    for key in words:
        if not is_noun(key):
            del copied[key]
    k = Counter(copied)
    return k.most_common(3)


def most_popular_words(name: str) -> list:
    """Gets 10 most common words in words list

    Args:
        name (str): Path to local pdf

    Returns:
        list: 10 words with most occurences
    """
    words = words_frequency(name)
    k = Counter(words)
    return k.most_common(10)
