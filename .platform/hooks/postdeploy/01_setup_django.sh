#!/bin/bash

if [[ $EB_IS_COMMAND_LEADER == "true" ]];
then
  source /var/app/venv/*/bin/activate

  if [[ -z "${DEPLOY_ENV}" ]]; then
    export ENV_VAR=$(/opt/elasticbeanstalk/bin/get-config environment)
  fi
  
  python3 manage.py migrate --noinput;
  python3 manage.py createsu;
  python3 manage.py migrate --noinput;
  python3 manage.py collectstatic --noinput;
else
    echo "this instance is NOT the leader"
fi