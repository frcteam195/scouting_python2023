cd ..
echo 'Running BA/eventsAll.py'
python3 ../BA/eventsAll.py -db dev1 -host aws
sleep 5

echo 'Running BA/totalTeamList.py'
python3 ../BA/totalTeamList.py -db dev1 -host aws
sleep 5