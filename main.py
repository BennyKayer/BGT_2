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