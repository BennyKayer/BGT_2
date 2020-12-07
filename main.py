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
from pathlib import Path

# Zaj 1
from zaj_01_20_11.count_words import count_words
from zaj_01_20_11.webScrapper import get_books

# Zaj 2
from zaj_02_23_11.most_popular_words import most_popular_nouns, most_popular_words

zaj_1 = False
zaj_2 = True

if zaj_1:
    get_books(
        "https://holybooks.com/the-complete-works-of-friedrich-nietzsche-in-english-as-pdf/",
        "nitsche",
    )
    folderName = "nitsche"

    total_words = 0
    p = Path(folderName)
    all_pdfs_paths = list(p.glob("*.pdf"))
    for b_p in all_pdfs_paths:
        total_words += count_words(os.path.join(folderName, b_p.name))
        print(total_words)
    print(f"In total Friedrich Nietzsche wrote {total_words}")

if zaj_2:
    # get_books("https://holybooks.com/sigmund-freud-the-complete-works/", 'freud')
    folderName = "freud"
    most_popular = {}
    most_popular_ns = {}
    p = Path("./freud")
    for b_p in list(p.glob("*.pdf")):
        most_popular = most_popular_words(os.path.join(folderName, b_p.name))
        most_popular_ns = most_popular_nouns(os.path.join(folderName, b_p.name))
    print(f"Freud most popular words {most_popular}")
    print(f"Freud most popular nouns {most_popular_ns}")
