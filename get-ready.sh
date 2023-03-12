
#! /bin/bash

path=/home/team195/scouting_python2023
# activate the venv
source "$path"/venv/bin/activate
# change to the path so relative paths are all correct
cd "$path"

echo ''; echo '***** Running BA/BAschedule.py *****'
python "$path"/BA/CEschedule.py -db production -host localhost
python "$path"/BA/CEschedule.py -db production -host pi
python "$path"/BA/CEschedule.py -db production -host aws

echo ''; echo '***** Running createCEteams.py *****'
python "$path"/createCEteams.py -db production -host localhost
python "$path"/createCEteams.py -db production -host pi
python "$path"/createCEteams.py -db production -host aws

echo ''; echo '***** Running createCEteams.py *****'
python "$path"/createMatches.py -db production -host localhost
python "$path"/createMatches.py -db production -host pi
python "$path"/createMatches.py -db production -host aws

echo ''; echo '***** Running createCEteams.py *****'
python "$path"/createMatchScoutingRecords.py -db production -host localhost
python "$path"/createMatchScoutingRecords.py -db production -host pi
python "$path"/createMatchScoutingRecords.py -db production -host aws
