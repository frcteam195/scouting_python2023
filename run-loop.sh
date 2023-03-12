#! /bin/bash

i=1
while [ $i -le 5 ]
do
  echo "************************************************************"
  echo "Loop $i"
  ./run.sh
  i=$(( $i + 1 ))
done
