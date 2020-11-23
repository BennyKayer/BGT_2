__author__ = "Paweł Benkowski, Stanisław Lutkiewicz"
'''
main.py - main file to count and print all of Friedrich Nietzsche wrote
count_words.py - contains a function for counting words from pdf file's
webScrapper.py - downloads all Nietzsche works from web to folder as pdf file's
'''

from pathlib import Path
# Zaj 1
from zaj_01_20_11.count_words import count_words
from zaj_01_20_11.webScrapper import get_books

# Zaj 2
from zaj_02_23_11.most_popular_words import most_popular_words

zaj_1 = False
zaj_2 = True

if (zaj_1):
    get_books('https://holybooks.com/the-complete-works-of-friedrich-nietzsche-in-english-as-pdf/', 'nitsche')

    total_words = 0
    p = Path('nitsche')
    for b_p in (list(p.glob('*.pdf'))):
        total_words += count_words(b_p.name)
        print(total_words)
    print(f'In total Friedrich Nietzsche wrote {total_words}')

if (zaj_2):
    get_books("https://holybooks.com/sigmund-freud-the-complete-works/", 'freud')

    total_words = {}
    p = Path('freud')
    for b_p in (list(p.glob('*.pdf'))):
        total_words = most_popular_words(b_p.name)
        print(total_words)
    print(f'Freud {total_words}')
    
    

