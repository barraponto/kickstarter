#!/bin/bash -
#===============================================================================
#
#          FILE: kickstart.sh
#
#         USAGE: ./kickstart.sh
#
#        AUTHOR: Capi Etheriel (barraponto@gmail.com)
#  ORGANIZATION: Hackatoa
#       CREATED: 05/23/2019 08:20:19 PM
#
#===============================================================================
set -o nounset                                  # Treat unset variables as an error
set -o xtrace

mkdir data
wget https://s3.amazonaws.com/weruns/forfun/Kickstarter/Kickstarter_2019-04-18T03_20_02_220Z.json.gz
gunzip -c Kickstarter_2019-04-18T03_20_02_220Z.json.gz > ./data/kickstarter.json
time python ./json_to_csv.py # creates ./data/kickstarter.csv
time pipenv run csvgrep -c country -m US -z 524288 ./data/kickstarter.csv > ./data/us.csv
time python ./data_cleaner.py # creates ./data/us-clean.csv
time pipenv run csvgrep -c launched_at,deadline -r '^201[4-8]' -z 524288 ./data/us-clean.csv > ./data/us-years.csv
time pipenv run csvcut -c id -z 524288 ./data/us-years.csv | sort | uniq -d > ./data/dupes-ids.csv
time pipenv run csvgrep -c id -f ./data/dupes-ids.csv -z 524288 ./data/us-years.csv | pipenv run csvsort -z 524288 -c id > ./data/dupes.csv
time pipenv run csvgrep -c id -f ./data/dupes-ids.csv -i -z 524288 ./data/us-years.csv > ./data/deduped.csv
time python ./dedupe.py # appends deduped.csv with deduped rows
cd kickstarter
pipenv run scrapy crawl -a file=../data/deduped.csv -o ../data/scraped.csv ksdata
