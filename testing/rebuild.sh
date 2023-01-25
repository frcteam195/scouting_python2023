#! /bin/bash
cwd=$(pwd)
echo $cwd

echo 'Running BA/eventsAll.py'
python3 $cwd/../BA/eventsAll.py -db dev1 -host aws
echo ''
sleep 2

echo 'Running BA/totalTeamList.py'
python3 $cwd/../BA/totalTeamList.py -db dev1 -host aws
echo ''
sleep 2

