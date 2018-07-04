#!/bin/bash

#this is the variable command because we may have different ips
# screen -d -m -S validator sudo -u sawtooth sawtooth-validator -v \
# --bind component:tcp://127.0.0.1:4004 \
# --bind network:tcp://172.31.81.231:8800 \
# --endpoint tcp://54.144.235.23:8800 \
# --peers tcp://34.239.121.66:8800,tcp://54.175.105.234:8800

screen -d -m -S validator sudo -u sawtooth sawtooth-validator -v
screen -d -m -S settings_tp sudo -u sawtooth settings-tp -v
screen -d -m -S poet_registry_tp sudo -u sawtooth poet-validator-registry-tp -v
screen -d -m -S rest_api sudo -u sawtooth sawtooth-rest-api -v
screen -d -m -S items_tp python3 /home/ubuntu/supplychain/Transaction_Families/sawtooth/proc/main.py tcp://127.0.0.1:4004
screen -d -m -S wallet_tp python3 /home/ubuntu/supplychain/Transaction_Families/wallet_tf/proc/main.py tcp://127.0.0.1:4004
screen -d -m -S server_django python3 /home/ubuntu/supplychain/webapp/manage.py runserver 0:8000