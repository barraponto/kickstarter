'''Cleans up some fields from webrobots csv dataset.'''
import csv
import json
from datetime import date


with open('./categories.json') as categories_file:
    CATEGORIES = json.load(categories_file)


def clean_data(row):
    '''Cleans a few columns from input rows.'''
    row = row.copy()
    row['category'] = CATEGORIES[row['source_url']]
    row['created_at'] = date.fromtimestamp(int(row['created_at'])).isoformat()
    row['deadline'] = date.fromtimestamp(int(row['deadline'])).isoformat()
    row['launched_at'] = date.fromtimestamp(int(row['launched_at'])).isoformat()
    try:
        row['location'] = json.loads(row['location'])['displayable_name']
    except json.JSONDecodeError:
        pass
    row['urls'] = json.loads(row['urls'])['web']['project']
    return row

def main():
    '''Cleans data from us.csv into us-clean.csv'''
    with open('./data/us.csv') as csvinput, open('./data/us-clean.csv', 'w') as csvoutput:
        reader = csv.DictReader(csvinput)
        writer = csv.DictWriter(csvoutput, reader.fieldnames)
        writer.writeheader()
        for row in reader:
            writer.writerow(clean_data(row))

if __name__ == "__main__":
    main()
