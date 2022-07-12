#!/bin/bash

if [[ $EB_IS_COMMAND_LEADER == "true" ]];
then
    source /var/app/venv/*/bin/activate 
    export ENV_VAR=$(/opt/elasticbeanstalk/bin/get-config environment)
else
    echo "this instance is NOT the leader"
fi