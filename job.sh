APP_HOME=/root/app
. $HOME/.profile
. /venv/bin/activate
cd $APP_HOME
export PYTHONPATH=$APP_HOME
python anoti/app.py
