# Juju  - Opérateur

Ceci est la partie pratique pour ceux qui veulent voir comment opérer sur un charm/bundle existant.

1. Bastion SSH/NAT

   1. Compte tenu que le cloud Maas est 'on-prem' et non sur le cloud, vos IPs seront locales. (ex. 172.16.66.23) - Il vous faudra soit :
      1. Passer par un tunnel SSH: [voir instructions](../juju/TunnelSshMaas.md)
      1. Demandez une redirection NAT : Assurez-vous de choisir un hostname - au besoin - avec n'importe quel sous-domaine *.ws1.lab-linux.com et fournissez votre IP privée et port

2. Choisissez un bundle pas trop gros

   1. Exemple: https://jaas.ai/wordpress/0
   2. Un trop gros bundle sera trop long à déployer pour cette atelier

3. Déployer et play with it !

   1. Suivez les instructions fournit par les créateurs du charms - ceci indique normalement comment déployer/scaler/changer de config, etc.



Quelques trucs:

- voir le status du modèle real-time: 

  ```
  watch -c juju status --color
  ```

- voir les logs du modèle

  ```
  juju debug-log
  juju debug-log --replay #Pour voir les anciens logs aussi
  ```

- ~~entrez pas ssh sur une machine en passant par juju~~ *ne semble pas fonctionner*

  ```
  juju ssh 0 #Machine ID
  juju ssh wordpress/1 #Unit
  ```

- la plupart des commandes en debug

  ```
  juju deploy cs:wordpress --debug
  ```

- enlever une application/machine/modèle

  ```
  juju remove-application wordpress
  juju remove-machine 0 #utilisez --force au besoin
  juju destroy-model MYMODELNAME #Attention ceci détruit tout, application, machine etc.
  ```

  

