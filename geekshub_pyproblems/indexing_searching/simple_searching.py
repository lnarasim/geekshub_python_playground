from json import load
from functools import reduce
import sys

INDEX_FILE = 'index.txt'
EMPTY_LIST = list()


# load the indices from the file and return a
# dictionary of index
def load_index(index_file):
    index_map = dict()
    try:
        with open(index_file) as file:
            index_map = load(file)
    except FileNotFoundError:
        pass
    return index_map


# This simple method returns your search results sorted
def search_word(word, index_map):
    if word in index_map:
        items = index_map[word]
        return sorted(items, key=lambda key: items[key], reverse=True)
    return EMPTY_LIST


# Search word with logic AND
def search_words_and(words, index_map):
    set_of_matches = [set(search_word(word, index_map)) for word in words]
    lst = list(reduce(set.intersection, set_of_matches))
    return lst


# Search word with logic AND
def search_words_or(words, index_map):
    lst = list(reduce(set.union,
                      [set(search_word(word, index_map))
                       for word in words]))
    return lst


if __name__ == '__main__':
    # load the index from the file
    new_map = load_index(INDEX_FILE)
    for word in sys.argv[1:]:
        print(f'Searching for {word}')
        matches = search_word(word, new_map)
        if matches:
            print('Found in')
            print('\t', matches)
            print()
        else:
            print('Not Found')