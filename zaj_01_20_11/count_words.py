import re

import PyPDF2


def count_words(name: str) -> int:
    """
    Extacts text from given pdf and returns word count

    Args:
        name (str): Path to locacl pdf

    Returns:
        int: Number of words in pdf
    """
    fileReader = PyPDF2.PdfFileReader(name)

    words = 0
    for page in fileReader.pages:
        page_text = page.extractText()
        words_on_page = re.findall(r"\b[^\d\W]+\b", page_text)
        words += len(words_on_page)

    return words


def count_words_new(name: str) -> int:
    """Gets text from given pdf and returns words count

    Args:
        name (str): Path to pdf

    Returns:
        int: Number of words in pdf
    """
    words = 0
    with open(name) as reader:
        text = reader.read()
        words_on_page = re.findall(r"\b[^\d\W]+\b", text)
        words += len(words_on_page)

    return words
