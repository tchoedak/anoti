#!/bin/bash
source venv/bin/activate
cd /root/app

python migrate.py
crontab schedule
exec "$@"
