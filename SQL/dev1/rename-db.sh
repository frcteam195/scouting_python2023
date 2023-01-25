# script to rename the database in the SQL create table files

if [[ $# != 2 ]]; then
    echo 'you must enter the starting and ending database name'
    echo 'e.g. ./rename-db.sh dev1 dev2'
    exit 0
else
    find . -type f -name '*.sql' -exec sed -i 's/dev1/dev2/' {} \;
    echo ''
    echo 'removing and rebuilding all.sql with build.sh'
    echo ''
    rm -f ./all.sql
    ./build.sh
fi