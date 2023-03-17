#! /bin/bash

i=1
while [ $i -le 500 ]
do
  echo "************************************************************"
  echo "Loop $i"
  ./run.aws.sh
  i=$(( $i + 1 ))
  sleep 60
done
