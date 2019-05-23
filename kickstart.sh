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

wget https://s3.amazonaws.com/weruns/forfun/Kickstarter/Kickstarter_2018-12-13T03_20_05_701Z.zip
unzip Kickstarter_2018-12-13T03_20_05_701Z.zip -d ./data
cat /data/Kickstarter*.csv | pipenv run csvgrep -c country -m US > ./data/usdata.csv
