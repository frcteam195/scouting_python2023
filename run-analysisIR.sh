#! /bin/bash

now=$(/bin/date +%Y-%m-%d_%H-%M)
echo '************************************************************'
echo $now
start_time=$(date +%s)

# define some variables ...
db=testing
remoteDB=testing # generally db and remoteDB will be the same, can be different for testing
host=localhost   # generally will be localhost. Using a variable for easy testing
remoteHost=aws   # generally will be aws, changeable here for testing
path=/home/ubuntu/scouting_python2023
# activate the venv
source "$path"/venv/bin/activate
# change to the path so relative paths are all correct
cd "$path"

echo ''; echo '***** Running analysisIR.py *****'
python "$path"/analysisIR.py -db "$db" -host "$host"

echo ''; echo '***** Running graphIR.py *****'
python "$path"/graphIR.py -db "$db" -host "$host"

end_time=$(date +%s)
elapsed=$(( end_time - start_time ))
echo '';echo "Total run time for run.sh: $elapsed seconds"; echo ''

deactivate
