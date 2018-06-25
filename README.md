# Blockchain for supply chain management

**Undergoing major overhaul check back in few days**

Note: Please have a glance over the sawtooth hyperledger architecture to make more sense out of this document.

## Introduction

This repository contains a web app that can be hosted on your ubuntu machine that talks with a sawtooth network. We defined few transaction families for our use, and those will be running on the validator node (More documentation to come explaining the transaction families).This project depends on
<ul> <li>Hyperledger sawtooth on Ubuntu 16.04 </li>
<li>Django 2.0 or later </li>
<li>screen</li>
</ul>

## Installation Procedure

First, install the dependencies as listed above. Once you create a sawtooth


## Details of folders

### Transaction Families

This folder cointains all the transaction processors in the current project. There are two transaction processors in the current project : sawtooth and wallet_tf. Each of the folders then have a **proc** folder and few scripts that can be run directly on the machine running the sawtooth validator (For debugging or other purposes). The proc folder then contains a transaction handler (smart contract equivalent), a script that takes care of state assignments and another script to unpack a transaction's payload.(Currently the payload is base64 encoded but in future we can add some encryption to it if necessary)

### Webapp

This folder has the django project that is used to host the current Active Release Platform. All the wrapping of transactions and creations are handled inside the items app of this project.

### RESTAPI

This folder contains an incomplete rest api. Currently not under development.