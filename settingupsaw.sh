#!/bin/bash

#this is the variable command because we may have different ips
screen -d -m -S validator sudo -u sawtooth sawtooth-validator -v \
--bind component:tcp://127.0.0.1:4004 \
--bind network:tcp://184.73.58.223:8800 \
--endpoint tcp://184.73.58.223:8800 \
--peers tcp://54.164.17.48:8800,tcp://18.206.225.151:8800


screen -d -m -S settings_tp sudo -u sawtooth settings-tp -v
screen -d -m -S poet_registry_tp sudo -u sawtooth poet-validator-registry-tp -v
screen -d -m -S rest_api sudo -u sawtooth sawtooth-rest-api -v
screen -d -m -S items_tp python3 /home/ubuntu/supplychain/Transaction_Families/sawtooth/proc/main.py
screen -d -m -S wallet_tp python3 /home/ubuntu/supplychain/Transaction_Families/wallet_tf/proc/main.py
screen -d -m -S server_django python3 /home/ubuntu/supplychain/webapp/manage.py runserver 0:8000