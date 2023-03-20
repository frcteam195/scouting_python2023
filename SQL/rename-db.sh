# script to rename the database in the SQL create table files
db1=$1
db2=$2

if [[ $# != 2 ]]; then
    echo 'you must enter the starting and ending database name'
    echo 'e.g. ./rename-db.sh dev1 dev2'
    exit 0
else
    find . -type f -name '*.sql' -exec sed -i "s/$db1/$db2/" {} \;
    echo ''
    echo 'removing and rebuilding all.sql with build.sh'
    echo ''
    rm -f ./all.sql
    ./build.sh
fi