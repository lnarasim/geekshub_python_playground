from json import dumps
import sys

URLS = ['1.txt', '2.txt']
INDEX_FILE = 'index.txt'
INDEX_MAP = dict()


# dump the index to the index file
def write_index_to_index_file(index_file, index_map):
    with open(index_file, "w") as index_file_obj:
        index_file_obj.write(dumps(index_map))


# build the index map, here we assume that all words
# have same key.
def build_index_map(index_map, words, key):
    for word in words:
        # word is already present in the index
        if word in index_map:
            values_dict = index_map[word]
            # The resource is already present, then
            # we need to probably update the counter
            if key in values_dict:
                values_dict[key] += 1
            else:
                values_dict[key] = 1
        else:
            # word is not present, we create and
            # set the counter to 1
            index_map[word] = dict()
            index_map[word][key] = 1


# Walk over the file and build index for each word
def read_build_index_file(index_map, filename):
    try:
        with open(filename) as file_obj:
            for line in file_obj:
                build_index_map(index_map, line.strip().split(), filename)
    except FileNotFoundError:
        print("File not found")


if __name__ == '__main__':
    files = sys.argv[1:]
    for file in files:
        read_build_index_file(INDEX_MAP, file)

    write_index_to_index_file(INDEX_FILE, INDEX_MAP)
