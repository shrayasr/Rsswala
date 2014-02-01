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
    printf "Usage: $0 mysqlusername mysqlpassword \n " && exit -1;
}

if [[ -z "$1" ]]; then
    display_help
fi

if [ "$1" = "help" ]; then
    display_help
fi

if [[ -z "$2" ]]; then
    display_help
fi

$MYSQLDUMP -u"$1" -p"$2" --no-data --skip-comments rsswala | sed 's/ AUTO_INCREMENT=[0-9]*\b//' > ./rsswala.sql

