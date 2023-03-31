#! /bin/bash

now=$(/bin/date +%Y-%m-%d_%H-%M)
echo '************************************************************'
echo $now
start_time=$(date +%s)

# define some variables ...
db=production
remoteDB=production # generally db and remoteDB will be the same, can be different for testing
host=localhost   # generally will be localhost. Using a variable for easy testing
remoteHost=aws   # generally will be aws, changeable here for testing
path=/home/ubuntu/scouting_python2023
# activate the venv
source "$path"/venv/bin/activate
# change to the path so relative paths are all correct
cd "$path"

echo ''; echo '***** Running BA/BAmatchData.py *****'
python "$path"/BA/BAmatchData.py -db "$db" -host "$host"

echo ''; echo '***** Running BA/BAoprs.py *****'
python "$path"/BA/BAoprs.py -db "$db" -host "$host"

echo ''; echo '***** Running BA/BAranks.py *****'
python "$path"/BA/BAranks.py -db "$db" -host "$host"

echo ''; echo '***** Running copyBAmatchData.py *****'
python "$path"/copyBAmatchData.py -db "$db" -host "$host"

echo ''; echo '***** Running insertFoulsRP.py *****'
python "$path"/insertFoulsRP.py -db "$db" -host "$host"

echo ''; echo '***** Running robotImages.py on AWS *****'
# ssh -i /home/team195/scouting.pem ubuntu@scouting.team195.com /home/ubuntu/scouting_python2023/robotImages.sh
python "$path"/robotImages.py

# echo ''; echo '***** Running syncTable to migrate matchScoutingL2 from aws to localhost *****'
# python "$path"/syncTable.py -db1 "$remoteDB" -host1 "$remoteHost" \
#   -db2 "$db" -host2 "$host" -table matchScoutingL2 -id matchScoutingL2ID

# echo ''; echo '***** Running syncTable to migrate pit from aws to localhost *****'
# python "$path"/syncTable.py -db1 "$remoteDB" -host1 "$remoteHost" \
#   -db2 "$db" -host2 "$host" -table pit -id pitID

echo ''; echo '***** Running analysisIR.py *****'
python "$path"/analysisIR.py -db "$db" -host "$host"

echo ''; echo '***** Running graphIR.py *****'
python "$path"/graphIR.py -db "$db" -host "$host"

echo ''; echo '***** Running scorePredict.py *****'
python "$path"/scorePredict.py -db "$db" -host "$host" -sb true

# echo ''; echo '***** Running syncTable to migrate matchScouting from localhost to aws *****'
# python "$path"/syncTable.py -db1 "$db" -host1 "$host" \
#   -db2 "$remoteDB" -host2 "$remoteHost" -table matchScouting -id matchScoutingID

# echo ''; echo '***** Running syncTable to migrate analysisTypes from localhost to aws *****'
# python "$path"/syncTable.py -db1 "$db" -host1 "$host" \
#   -db2 "$remoteDB" -host2 "$remoteHost" -table analysisTypes -id analysisTypeID -noCE true

# echo ''; echo '***** Running syncTable to migrate matches from localhost to aws *****'
# python "$path"/syncTable.py -db1 "$db" -host1 "$host" \
#   -db2 "$remoteDB" -host2 "$remoteHost" -table matches -id matchID

# mysqldump / mysql for data sync between localhost and aws
# mysqldump "$db" CEanalysis > dump.sql
# mysqldump "$db" CEanalysisGraphs >> dump.sql
# mysqldump "$db" dnpList >> dump.sql
# mysqldump "$db" final24 >> dump.sql
# mysqldump "$db" pickList1 >> dump.sql
# mysqldump "$db" watch1 >> dump.sql
# mysqldump "$db" watch2 >> dump.sql
# mysql -h scouting.team195.com "$remoteDB"  < dump.sql
# rm -f dump.sql

# share script for sharing L1 quantitative data
echo ''; echo '***** running share.py *****'
python "$path"/share.py -db "$db" -host "$host"
mv 195scoutingData.csv /media/shareData
mv 195scoutingData.json /media/shareData

# DB backup
echo ''; echo 'performing DB backup'
mkdir -p /home/ubuntu/DBbackups
cd /home/ubuntu/DBbackups
/usr/bin/mysqldump -h localhost "$db" > event_"$now".sql
/bin/tar -czf event_"$now".tgz event_"$now".sql
# cp event_"$now".sql /media/team195/SI-MEDIA
/bin/rm -f event_"$now".sql

# echo ''; echo 'secure copying csv and json file to website'
# /usr/bin/scp -i /home/team195/scouting.pem "$path"/195scoutingData.csv ubuntu@scouting.team195.com:/media/shareData
# /usr/bin/scp -i /home/team195/scouting.pem "$path"/195scoutingData.json ubuntu@scouting.team195.com:/media/shareData
# sleep 1
# rm -f "$path"/195scoutingData.csv "$path"/195scoutingData.json

end_time=$(date +%s)
elapsed=$(( end_time - start_time ))
echo '';echo "Total run time for run.sh: $elapsed seconds"; echo ''

deactivate
