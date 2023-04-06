#! /bin/bash

i=1
while [ $i -le 500 ]
do
  echo "************************************************************"
  echo "Loop $i"
  ./run.sh
  i=$(( $i + 1 ))
  sleep 10
done
