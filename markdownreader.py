#! /usr/bin/env python3
import os, sys
sys.path.append(os.path.dirname(__file__) + '/lib')

from bs4 import BeautifulSoup
from markdown2 import markdown

with open(sys.argv[1], 'r') as md_file:
    content = md_file.read()
    html = markdown(content)
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
    for title in soup.find_all('h2'):
        if title.string == 'Installation':
            ol = title.find_next_sibling('ol')
            for li in ol.find_all('li'):
                print(li.get_text())
