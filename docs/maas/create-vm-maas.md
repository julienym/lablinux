# Quickstart Maas-VM

Créer une VM sur MAAS sans compte administrateur se fait par le CLI.

## Requis

1. Compte MAAS
2. Machine ubuntu (ou un bastion) avec CLI de MAAS

## Configurer son cli 

https://maas.io/docs/maas-cli

1. Downloader le client maas sur votre poste, ou sur le bastion

2. Créer une clef API pour votre client maas (CLI)

   1. Connectez vous sur https://maas.lab-linux.com/ avec votre compte
   2. En haut à droite, cliquez sur votre username
   3. Generate MAAS key - copier cette nouvelle clef

3. Avec le cli de maas: 

   ```maas login maas-lab https://maas.lab-linux.com/MAAS/```

Notez que maas-lab peut s'appeler comme vous voulez, c'est un nom de profile de connection

4. Vérifier vos profiles et clefs API avec

   ```maas list```

## Créer une VM

https://maas.io/docs/cli-composable-machines-management

1. La commande de base pour s'allouer une VM:

   ```maas maas-lab machines allocate pod=***** interfaces=eth0:space=*******```

   **space**=<l'espace réseau qui vous a été attitré> ou maas pour le réseau partagé

   *optionnel* **pod**=host KVM qui vous attitré

   Si vous ne mentionnez rien d'autre, la VM aura 1 vcpu, 1gb de ram et 8gb de disque dur

2. Rajouter d'autres options:

    **cpu_count=** requested cores
    **mem=** requested memory in MB
    **storage=storage pool:GB** (si le host a plusieurs storage pool de disponible)

Exemple:

```
maas maas-lab machines allocate interfaces=eth0:space=****** cpu_count=2 mem=4096 storage=maas:80
```

3. Votre VM sera ensuite disponible par le bastion (voir config SSH)

   ```
ssh polite-cub.******
   ```
   