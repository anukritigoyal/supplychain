screen -d -m -S keygeneration sawtooth keygen
screen -d -m -S validator_key_gen sudo sawadm keygen

sudo chmod -R 777 /var/lib/sawtooth
sudo sawset genesis -k /etc/sawtooth/keys/validator.priv -o config-genesis.batch

sudo sawset proposal create -k /etc/sawtooth/keys/validator.priv \
-o config.batch \
sawtooth.consensus.algorithm=poet \
sawtooth.poet.report_public_key_pem="$(cat /etc/sawtooth/simulator_rk_pub.pem)" \
sawtooth.poet.valid_enclave_measurements=$(poet enclave measurement) \
sawtooth.poet.valid_enclave_basenames=$(poet enclave basename) \
sawtooth.poet.ztest_minimum_win_count=99999999

poet registration create -k /etc/sawtooth/keys/validator.priv -o poet.batch

sawset proposal create -k /etc/sawtooth/keys/validator.priv \
-o poet-settings.batch \
sawtooth.poet.target_wait_time=5 \
sawtooth.poet.initial_wait_time=25 \
sawtooth.publisher.max_batches_per_block=100


sawadm genesis config-genesis.batch config.batch poet.batch poet-settings.batch


screen -d -m -S settings_tp sudo -u sawtooth settings-tp -v
screen -d -m -S poet_registry_tp sudo -u sawtooth poet-validator-registry-tp -v
screen -d -m -S rest_api sudo -u sawtooth sawtooth-rest-api -v
screen -d -m -S items_tp python3 /home/ubuntu/supplychain/Transaction_Families/sawtooth/proc/main.py
screen -d -m -S wallet_tp python3 /home/ubuntu/supplychain/Transaction_Families/wallet_tf/proc/main.py
screen -d -m -S server_django python3 /home/ubuntu/supplychain/webapp/manage.py runserver 0:8000
screen -d -m -S validator sudo -u sawtooth sawtooth-validator -v