# Tunnel SSH - MAAS

1. Tunnel SSH:

   1. Pour les utilisateurs Windows/Putty - considérer installer LinuxWSL (Win10) ou VirtualBox avec une VM Linux - et sinon voir l'option NAT

      1. Clef SSH avec Putty: https://www.ssh.com/ssh/putty/windows/puttygen
      2. Tunnel SSH : https://blog.devolutions.net/2017/4/how-to-configure-an-ssh-tunnel-on-putty

   2. Fournir votre clef publique à MAAS

      1. Connectez-vous au compte workshop01 sur https://maas.lab-linux.com/
      2. Cliquez sur votre nom utilisateur dans le coin en haut à droite
      3. Importez ou uploader votre clef ssh
      4. Les machines doréavant créées avec ce compte - lier au controlleur Juju - auront votre clef

   3. Pour Mac/Linux, rajouter cette config dans votre ~/.ssh/config

      1. ```
         #WORKSHOP1 - JUJU-MAAS
         Host bastion.ws1.lab-linux.com 
           Port 22011
           User ubuntu
           ControlMaster auto
           ControlPersist 600  
           IdentityFile ~/.ssh/juju-workshop01
         
         Host *.maas
           User ubuntu
           IdentityFile ~/.ssh/VOTRECLEFPUBLIC
           ProxyJump bastion.ws1.lab-linux.com
         ```

      2. Rajouter la clef privé dans votre dossier ~/.ssh/juju-workshop01

      3. Vous pouvez maintenant vous connectez à un machine .maas facilement

      4. Pour ouvrir un tunnel local:

         1. ```
            ssh -N bastion.ws1.lab-linux.com -L 8888:(172.16.66.78|hostname.maas):80
            ```
