#!/bin/bash

if [[ $EB_IS_COMMAND_LEADER == "true" ]];
then
  source /var/app/venv/*/bin/activate
  export ENV_VAR=$(/opt/elasticbeanstalk/bin/get-config environment)
  python3 manage.py migrate --noinput;
  python3 manage.py collectstatic --noinput;
else
    echo "this instance is NOT the leader"
fi