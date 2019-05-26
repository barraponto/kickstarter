'''Dedupes rows by source_url field'''
import csv
from itertools import zip_longest


def grouper(iterable, chunk_size, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * chunk_size
    return zip_longest(*args, fillvalue=fillvalue)


def dedupe(dupe_a, dupe_b):
    '''Picks dupe with longer source_url value.'''
    if len(dupe_a['source_url']) > len(dupe_b['source_url']):
        return dupe_a
    else:
        return dupe_b


def main():
    '''Reads dupes from a file and outputs dedupes to another file.'''
    with open('./data/dupes.csv') as dupesinput, open('./data/deduped.csv', 'a') as dupesoutput:
        reader = csv.DictReader(dupesinput)
        writer = csv.DictWriter(dupesoutput, reader.fieldnames)
        for dupe_a, dupe_b in grouper(reader, 2):
            writer.writerow(dedupe(dupe_a, dupe_b))


if __name__ == "__main__":
    main()
