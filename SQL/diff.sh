# script to look for differences in DB SQL scripts
db1="$1"
db2="$2"

if [[ $# != 2 ]]; then
    echo 'you must enter the starting and ending database name'
    echo 'e.g. ./rename-db.sh dev1 dev2'
    exit 0
else
    db1_count=$(ls "$db1"/*.sql | awk '!/all.sql/' | wc -l)
    db2_count=$(ls "$db2"/*.sql | awk '!/all.sql/' | wc -l)
    echo "$db1 has $db1_count SQL files, excluding all.sql"
    echo "$db2 has $db2_count SQL files, excluding all.sql"
fi
