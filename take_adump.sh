#!/bin/bash

# takes a mysqldump of the rsswala database
# stripsoff the autoincrement values

MYSQLDUMP=$(which mysqldump)

if [ $? != 0 ]; then
  echo "mysqldump not found, is it in your path?"
  exit 1
fi

display_help ()
{
    printf "Usage: $0 mysqlusername [mysqlpassword] \n " && exit -1;
}

if [[ -z "$1" ]]; then
    display_help
fi

if [ "$1" = "help" ]; then
    display_help
fi

PASS="-p"

if [ -n "$2" ]; then
    PASS=-p"$2"
fi

$MYSQLDUMP -u"$1" $PASS --no-data rsswala | sed 's/ AUTO_INCREMENT=[0-9]*\b//' > ./rsswala.sql

