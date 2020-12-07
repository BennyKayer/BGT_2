#!/usr/bin/env python
# coding: utf-8

# In[2]:


import sys
get_ipython().system('{sys.executable} -m pip install PyPDF2')
get_ipython().system('{sys.executable} -m pip install requests')
get_ipython().system('{sys.executable} -m pip install bs4')


# In[ ]:


from pyspark import SparkContext, SparkFiles

import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup

import PyPDF2
import re
from collections import Counter


# In[ ]:


folderName = 'freud'
get_books("https://holybooks.com/sigmund-freud-the-complete-works/", folderName)

p = Path(folderName)
print(p)
pdfFiles = list(p.glob('*.pdf'))
for b_p in pdfFiles:
    save_text_from_pdf(os.path.join(folderName, b_p.name))


# In[4]:





def get_books(url, target):
    if not os.path.isdir(target):
        os.makedirs(target)

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    for a in soup.find_all("a", href=True):
        arr = a["href"].split(".")
        if arr[-1] == "pdf":
            response = requests.get("http:" + a["href"])
            with open(Path(target, a.string + ".pdf"), "wb+") as f:
                f.write(response.content)


def save_text_from_pdf(name):
    fileReader = PyPDF2.PdfFileReader(name)
    with open(Path(name + ".txt"), "a+") as f:
        for page in fileReader.pages:
            f.write(page.extractText())


def words_frequency(page_text):
    words = {}
    words_list = re.findall(r"\b[^\d\W]+\b", page_text)
    print(page_text)
    for word in words_list:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    return words


def most_popular_words(name):
    words = words_frequency(name)
    print(words)
    k = Counter(words)
    return k.most_common(10)



sc = SparkContext("local", "first app")
p = Path(folderName)
allTextFiles = list(p.glob('*.txt'))
files = []
for b_p in allTextFiles:
    files.append(sc.textFile(os.path.join(folderName, b_p.name)).cache())

for file in files:
#     numXs = file.filter(lambda s: 'x' in s).count()
#     numYs = file.filter(lambda s: 'y' in s).count()
#     print(numXs, numYs)
    mostPopular = most_popular_words(file)
    print(mostPopular)


# In[15]:


from operator import add


# In[37]:


for file in files:
#     numXs = file.filter(lambda s: 'x' in s).count()
#     numYs = file.filter(lambda s: 'y' in s).count()
#     print(numXs, numYs)
#     print(file.collect()[:10])
    a = file.map(lambda x : re.findall(r"\b[^\d\W]+\b", x))
    a = a.flatMap(lambda x: x)
    a = a.map(lambda x: (x,1))
    b = a.collect()
    print(b[:10])
    c =a.reduceByKey(add).collect()
    print(c)
    print(a.count())
    
#     mostPopular = most_popular_words(file)
#     print(mostPopular)


# In[ ]:




