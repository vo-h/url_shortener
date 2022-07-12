#!/bin/bash

if [[ $EB_IS_COMMAND_LEADER == "true" ]];
then
  python manage.py migrate --noinput;
  python manage.py collectstatic --noinput;
else
    echo "this instance is NOT the leader"
fi