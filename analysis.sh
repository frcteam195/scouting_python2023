now=$(date +%Y-%m-%d_%H-%M)
cd /home/team195/DBbackups
/usr/bin/mysql -h localhost dev1 > event_"$now".sql
/bin/tar -czf event_"$now".tgz event_"$now".sql
/bin/rm -f event_"$now".sql
