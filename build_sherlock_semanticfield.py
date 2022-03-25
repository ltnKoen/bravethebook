#!/usr/bin/env python3

import urllib.request
from bs4 import BeautifulSoup
from unidecode import unidecode
from itertools import chain

def read_titles_on_page(url):
    with urllib.request.urlopen(url) as response:
        page = response.read()
    soup = BeautifulSoup(page, 'html.parser')
    elements = soup.find(lambda tag: tag.name == 'ul' and tag.get('class') == ['mw-allpages-chunk']) # <ul class="mw-allpages-chunk">
    for element in elements.children:
        if hasattr(element, 'children'):
            yield next(element.children)['title']

# first_url = 'https://bakerstreet.fandom.com/wiki/Special:AllPages'
# next_url = lambda t: 'https://bakerstreet.fandom.com/wiki/Special:AllPages?from=' + t.replace(' ', '+')

def read_all_titles(first_url, next_url):
    group = list(read_titles_on_page(first_url))
    groups = [group]
    while len(group) > 1:
        last_title_on_page = group[-1]
        url = next_url(last_title_on_page)
        group = list(read_titles_on_page(url))
        groups.append(group)
    return list(chain.from_iterable(groups))

def clean_names(titles):
    names = [name.rsplit('/', maxsplit=1)[-1].lower() for name in titles]
    names = [name.split('(', maxsplit=1)[0].strip() for name in names]
    names = list(set(map(unidecode, names)))
    #names = list(set(names + [name for sentence in names for name in sentence.split()]))
    return names

def write_words(filename, words):
    with open(filename, 'w') as f:
        f.write('\n'.join(words))

from os import path

def main():
    first_url = 'https://bakerstreet.fandom.com/wiki/Special:AllPages'
    next_url = lambda t: 'https://bakerstreet.fandom.com/wiki/Special:AllPages?from=' + t.replace(' ', '+')
    subfolder, filename = 'resources', 'sherlockholmes_english.txt'
    filename = path.join(subfolder, filename)
    print('Fetching data from: ', first_url)
    titles = read_all_titles(first_url, next_url)
    print('Done fetching data. Cleaning names.')
    names = clean_names(titles)
    print('Done cleaning. Writing results to: ', filename)
    write_words(filename, names)
    print('Wrote results to: ', filename)

if __name__ == '__main__':
    main()
