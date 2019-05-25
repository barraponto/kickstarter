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
python ./json_to_csv.py
#cat data/Kickstarter*.csv | pipenv run csvgrep -c country -m US -z 524288 > ./data/usdata.csv
#cd kickstarter
#pipenv run scrapy crawl -a file=../data/usdata.csv -o ../data/data.csv ksdata
