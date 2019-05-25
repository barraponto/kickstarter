'''Converts webrobots.io kickstarter json dataset into proper csv.'''
import csv
import json

from fields import FIELDS, JSON_FIELDS


def json_dump_fields(project):
    '''Properly json dumps extended data fields for csv files.'''
    project = project.copy()
    for field in JSON_FIELDS:
        try:
            project[field] = json.dumps(project[field])
        except KeyError:
            pass
    return project

def main():
    '''Writes csv file from the json file.'''
    with open('./data/kickstarter.json') as jsoninput, open('./data/kickstarter.csv', 'w') as csvoutput:
        writer = csv.DictWriter(csvoutput, FIELDS)
        writer.writeheader()
        for project in jsoninput:
            project = json.loads(project)
            writer.writerow(json_dump_fields(project['data']))

if __name__ == "__main__":
    main()
