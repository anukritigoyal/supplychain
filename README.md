# Blockchain for supply chain management
**Undergoing major overhaul check back in few days**

##Transaction Families

This folder cointains all the transaction processors in the current project. There are two transaction processors in the current project:sawtooth and  


## Sawtooth

The sawtooth folder contains a 'hello world' transcation family which create a client that can create an item, send the item from one client to other, or perform some checks on the item(Depending upon its privileges that are stored inside the wallet transcation family) .
#####
## Wallet_tf

This folder contains a 'wallet' transaction family which maintains the public keys of the client applications in the sawtooth framework itself. Wallet tf also stores the profiles of the client.
######
**P.S.** : **proc** folder has the transaction processor part and the scripts outside it pertain to the client.
