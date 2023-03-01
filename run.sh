#! /bin/bash

# define some variables ...
db=dev2
remoteDB=testing    # generally db and remoteDB will be the same, can be different for testing
host=aws    # generally will be localhost. Using a variable for easy testing
remoteHost=aws  # generally will be aws, changeable here for testing
path=/Users/markmaciejewski/robotics/scouting_python2023
# activate the venv
source "$path"/venv/bin/activate
# change to the path so relative paths are all correct
cd "$path"

# echo ''; echo '***** Running BA/BAmatchData.py *****'
# python "$path"/BA/BAmatchData.py -db "$db" -host "$host"

# echo ''; echo '***** Running BA/BAoprs.py *****'
# python "$path"/BA/BAoprs.py -db "$db" -host "$host"

# echo ''; echo '***** Running BA/BAranks.py *****'
# python "$path"/BA/BAranks.py -db "$db" -host "$host"

# echo ''; echo '***** Running copyBAmatchData.py *****'
# python "$path"/copyBAmatchData.py -db "$db" -host "$host"

# echo ''; echo '***** Running insertFoulsRP.py *****'
# python "$path"/insertFoulsRP.py -db "$db" -host "$host"

# echo ''; echo '***** Running syncTable to migrate matchScoutingL2 from aws to localhost *****'
# python "$path"/syncTable.py -db1 "$remoteDB" -host1 "$remoteHost" \
#   -db2 "$db" -host2 "$host" -table matchScoutingL2 -id matchScoutingL2ID

# echo ''; echo '***** Running syncTable to migrate pit from aws to localhost *****'
# python "$path"/syncTable.py -db1 "$remoteDB" -host1 "$remoteHost" \
#   -db2 "$db" -host2 "$host" -table pit -id pitID

# echo ''; echo '***** Running analysisIR.py *****'
# python "$path"/analysisIR.py -db "$db" -host "$host"

echo ''; echo '***** Running graphIR.py *****'
python "$path"/graphIR.py -db "$db" -host "$host"

echo ''; echo '***** Running syncTable to migrate matchScouting from localhost to aws *****'
python "$path"/syncTable.py -db1 "$db" -host1 "$host" \
  -db2 "$remoteDB" -host2 "$remoteHost" -table matchScouting -id matchScoutingID

echo ''; echo '***** Running syncTable to migrate matches from localhost to aws *****'
python "$path"/syncTable.py -db1 "$db" -host1 "$host" \
  -db2 "$remoteDB" -host2 "$remoteHost" -table matches -id matchID

# DB backup
# mkdir -p /home/team195/DBbackups
# now=$(/bin/date +%Y-%m-%d_%H-%M)
# cd /home/team195/DBbackups
# /usr/bin/mysqldump -h localhost "$db" > event_"$now".sql
# /bin/tar -czf event_"$now".tgz event_"$now".sql
# /bin/rm -f event_"$now".sql

deactivate

