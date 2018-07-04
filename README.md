# Blockchain for supply chain management

**Undergoing major overhaul check back in few days**

Note: Please have a glance over the sawtooth hyperledger architecture to make more sense out of this document.

## Introduction

This repository contains a web app that can be hosted on your ubuntu machine that talks with a sawtooth network. We defined few transaction families for our use, and those will be running on the validator node (More documentation to come explaining the transaction families).This project depends on
<ul> <li>Hyperledger sawtooth on Ubuntu 16.04 </li>
<li>Django 2.0 or later </li>
<li>screen</li>
<li>git</li>
</ul>

**Note: Docker compatibility is in works**

## Installation Procedure

### Installation of hyperledger-sawtooth

```shell
user@validator$ sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 8AA7AF1F1091A5FD
user@validator$ sudo add-apt-repository 'deb [arch=amd64] http://repo.sawtooth.me/ubuntu/1.0/stable xenial universe'
user@validator$ sudo apt-get update
user@validator$ sudo apt-get install -y sawtooth
```

### Generate User Key and validator key

Generate an user key with

```shell
user@validator$ sawtooth keygen
```

Generate a validator private key with

```shell
user@validator$ sudo sawadm keygen
```

### Genesis block creation

Creation of the first block in the block chain and the subsequent setting of poet consensus algo are shown below.

```shell
sawset genesis -k /etc/sawtooth/keys/validator.priv -o config-genesis.batch && \
sawset proposal create -k /etc/sawtooth/keys/validator.priv \
-o config.batch \
sawtooth.consensus.algorithm=poet \
sawtooth.poet.report_public_key_pem="$(cat /etc/sawtooth/simulator_rk_pub.pem)" \
sawtooth.poet.valid_enclave_measurements=$(poet enclave measurement) \
sawtooth.poet.valid_enclave_basenames=$(poet enclave basename) && \
poet registration create -k /etc/sawtooth/keys/validator.priv -o poet.batch && \
sawset proposal create -k /etc/sawtooth/keys/validator.priv \
-o poet-settings.batch \
sawtooth.poet.target_wait_time=5 \
sawtooth.poet.initial_wait_time=25 \
sawtooth.publisher.max_batches_per_block=100 && \
sawadm genesis config-genesis.batch config.batch poet.batch poet-settings.batch 
```

Note:To make a better sense out of the above steps please refer [Sawtooth documentation](https://sawtooth.hyperledger.org/docs/core/nightly/master/app_developers_guide/creating_sawtooth_network.html)

### Starting the first validator

Before we start the first validator, since we are creating a network of validators, find out the local ip of the machine and its public endpoint.Now start the validator with

```shell
sawtooth-validator -v \
    --bind network:tcp://(your local ip):8800 \
    --bind component:tcp://(your local ip):4004 \
    --peering dynamic \
    --endpoint tcp://(your public endpoint):8800 \
    --scheduler serial \
    --network trust
```

### Adding rest api and default transaction processors

Open a new terminal window (or a screen session) and start the rest-api of sawtooth framework with:

```shell
$ sudo -u sawtooth sawtooth-rest-api -v
```



## Details of folders

### Transaction Families

This folder cointains all the transaction processors in the current project. There are two transaction processors in the current project : sawtooth and wallet_tf. Each of the folders then have a **proc** folder and few scripts that can be run directly on the machine running the sawtooth validator (For debugging or other purposes). The proc folder then contains a transaction handler (smart contract equivalent), a script that takes care of state assignments and another script to unpack a transaction's payload.(Currently the payload is base64 encoded but in future we can add some encryption to it if necessary)

### Webapp

This folder has the django project that is used to host the current Active Release Platform. All the wrapping of transactions and creations are handled inside the items app of this project.

### RESTAPI

This folder contains an incomplete rest api. Currently not under development.
