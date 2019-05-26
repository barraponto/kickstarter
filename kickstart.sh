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

mkdir data
wget https://s3.amazonaws.com/weruns/forfun/Kickstarter/Kickstarter_2019-04-18T03_20_02_220Z.json.gz
gunzip -c Kickstarter_2019-04-18T03_20_02_220Z.json.gz > ./data/kickstarter.json
python ./json_to_csv.py # creates ./data/kickstarter.csv
pipenv run csvgrep -c country -m US -z 524288 ./data/kickstarter.csv > ./data/us.csv
python ./data_cleaner.py # creates ./data/us-clean.csv
#pipenv run csvgrep -c launched_at,deadline -r '^201[4-8]' -z 524288 ./data/us.csv > ./data/us-years.csv
#cd kickstarter
#pipenv run scrapy crawl -a file=../data/usdata.csv -o ../data/data.csv ksdata
