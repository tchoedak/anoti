#!/bin/bash
APP_HOME=/root/app
. $HOME/.profile
. /root/app/.env
. /venv/bin/activate
cd $APP_HOME
export PYTHONPATH=$APP_HOME
python anoti/app.py pulse 60 &
