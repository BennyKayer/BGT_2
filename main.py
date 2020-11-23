__author__ = "Paweł Benkowski, Stanisław Lutkiewicz"
'''
main.py - main file to count and print all of Friedrich Nietzsche wrote
count_words.py - contains a function for counting words from pdf file's
webScrapper.py - downloads all Nietzsche works from web to folder as pdf file's
'''

from pathlib import Path
from count_words import count_words
from webScrapper import get_books


get_books()

total_words = 0
p = Path('.')
for b_p in (list(p.glob('*.pdf'))):
    total_words += count_words(b_p.name)
    print(total_words)
print(f'In total Friedrich Nietzsche wrote {total_words}')
