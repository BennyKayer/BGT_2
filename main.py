__author__ = "Paweł Benkowski, Stanisław Lutkiewicz"
"""
main.py - main file \
            -  download count and print all of Friedrich Nietzsche wrote \
            -  download, find top 10 words and top 3 nouns
zaj_01_20_11/count_words.py - contains a function for counting words from pdf file's
zaj_01_20_11/webScrapper.py - downloads all Nietzsche works from web to folder as pdf file's
zaj_02_23_11/webScrapper.py - counts most popular nouns and words
"""
import os
import timeit
from pathlib import Path

# Zaj 1
from zaj_01_20_11.count_words import count_words_new
from zaj_01_20_11.webScrapper import get_pfds_and_extract_to_text

# Zaj 2
from zaj_02_23_11.most_popular_words import most_popular_nouns, most_popular_words

zaj_1 = False
zaj_2 = True

if zaj_1:
    folderName = "nitsche"
    url = "https://holybooks.com/sigmund-freud-the-complete-works/"
    total_words = 0
    get_pfds_and_extract_to_text(url, folderName)
    p = Path(folderName)
    for b_p in list(p.glob("*.txt")):
        total_words += count_words_new(os.path.join(folderName, b_p.name))
        print(total_words)
    print(f"In total Friedrich Nietzsche wrote {total_words}")

if zaj_2:
    folderName = "freud"
    url = "https://holybooks.com/sigmund-freud-the-complete-works/"
    most_popular = {}
    most_popular_ns = {}
    total_words = 0
    get_pfds_and_extract_to_text(url, folderName)
    p = Path(folderName)
    start = timeit.default_timer()
    for b_p in list(p.glob("*.txt")):
        most_popular = most_popular_words(os.path.join(folderName, b_p.name))
        most_popular_ns = most_popular_nouns(os.path.join(folderName, b_p.name))
        total_words += count_words_new(os.path.join(folderName, b_p.name))
    end = timeit.default_timer()
    print(end - start)
    print(f"Freud most popular words {most_popular}")
    print(f"Freud most popular nouns {most_popular_ns}")
    print(f"Freud total words {total_words}")
