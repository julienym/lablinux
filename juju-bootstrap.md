*en construction*

# Quickstart Juju-Controller

**Pour créer un contrôlleur Juju, vous devez pouvoir vous connecter à la VM qui l'hébergera. Vous devez donc utiliser un bastion SSH. Voir ...**

Si vous voulez que ce contrôlleur soit accessible de l'extérieur, il vous faudra une IP privée. Commandez ici ...

## Requis

1. Compte MAAS
   1. Créer une clef API pour Juju
2. Bastion SSH

## Configurer son cli 

https://jaas.ai/docs/installing

1. Downloader le client juju sur votre poste, ou sur le bastion

2. Rajouter le cloud Maas

   ```juju add-cloud
   $ juju add-cloud
   Cloud Types
     lxd
     maas
     manual
     openstack
     vsphere
   
   Select cloud type: maas
   
   Enter a name for your maas cloud: maas-lab
   
   Enter the API endpoint url: https://maas.lab-linux.com/MAAS/
   
   You will need to add credentials for this cloud (`juju add-credential maas-lab`)
   before creating a controller (`juju bootstrap maas-lab`).
   ```

3. Rajouter l'authentification créer plutôt dans MAAS

   ```
   $ juju add-credential maas-lab
   Enter credential name: maas-lab-creds
   
   Using auth-type "oauth1".
   
   Enter maas-oauth: *** API KEY FROM MAAS ***
   
   Credential "maas-lab-creds" added locally for cloud "maas-lab".
   ```

4. Créer un controlleur Juju pour votre cloud Maas

   https://jaas.ai/docs/creating-a-controller
   
   ```
$ juju bootstrap maas-lab --?
   ```
   
   Note: bootstrap utilisera une machine ou VM dans MAAS de libre (ready ou allocated) qui a le minimum requis: 1 vcpu et 3.5Gb de ram
   
   Pour choisir sur quelle machine déployer le contrôleur Juju:
   
   ```
   juju bootstrap maas-lab --to hostname.maas
   ```
   
   
