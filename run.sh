#! /bin/bash

db=dev2
host=aws
path=/Users/markmaciejewski/robotics/scouting_python2023
echo $db
echo $host

source "$path"/venv/bin/activate
echo $PATH

python "$path"/BA/BAmatchData.py -db "$db" -host "$host"

echo $PATH

# DB backup
# mkdir -p /home/team195/DBbackups
# now=$(/bin/date +%Y-%m-%d_%H-%M)
# cd /home/team195/DBbackups
# /usr/bin/mysqldump -h localhost "$db" > event_"$now".sql
# /bin/tar -czf event_"$now".tgz event_"$now".sql
# /bin/rm -f event_"$now".sql

