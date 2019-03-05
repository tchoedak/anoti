#!/bin/bash
echo "SMTP_USERNAME=$SMTP_USERNAME" >> /etc/environment
echo "SMTP_PASSWORD=$SMTP_PASSWORD" >> /etc/environment
echo "SELLER_CENTRAL_ACCESS_KEY_ID=$SELLER_CENTRAL_ACCESS_KEY_ID" >> /etc/environment
echo "SELLER_CENTRAL_SECRET_KEY=$SELLER_CENTRAL_SECRET_KEY" >> /etc/environment
echo "ACCOUNT_SID=$ACCOUNT_SID" >> /etc/environment
echo "AUTH_TOKEN=$AUTH_TOKEN" >> /etc/environment
echo "ANOTI_NUMBER=$ANOTI_NUMBER" >> /etc/environment


. /root/app/.env
. $HOME/.profile
source /venv/bin/activate
cd /root/app
pip install .

python migrate.py
anoti pulse 60 &
exec "$@"
