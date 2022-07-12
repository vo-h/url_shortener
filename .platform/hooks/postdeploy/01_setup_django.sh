#!/bin/bash

if [[ $EB_IS_COMMAND_LEADER == "true" ]];
then
  python3 manage.py migrate --noinput;
  python3 manage.py collectstatic --noinput;
else
    echo "this instance is NOT the leader"
fi