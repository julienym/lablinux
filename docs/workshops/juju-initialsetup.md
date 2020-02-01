# Juju - initial setup

**But**: installer le cli juju et s'authentifier avec le controlleur juju déjà fournit + création d'un modèle

- Installer juju
  - https://jaas.ai/docs/installing
- Connectez-vous avec le token fournit
  - juju register XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  - Vous serez à rentrer un mot de passe
- Vérifier votre controlleur
  - juju list-controllers
- Rajouter le cloud et le credential pour celui-ci
  - juju add-cloud lablinux -f lablinux-creds.yaml --client
  - juju add-credentials lablinux -f lablinux-creds.yaml --client
- Créer son modèle (espace de travail) et définir l'espace réseau par défaut
  - juju add-model VOTRENOM
  - juju set-model-constraints spaces=maas
- (bonus) Rajouter sa clef SSH publique au modèle pour pouvoir accèder aux machines créées
  - Si votre clef est déjà sur github: juju import-ssh-key gh:USERNAME
  - Sinon: juju add-ssh-key "VOTRE CLEF PUBLIQUE" ou utiliser "$(cat ~/mykey.pub)"
- *(bonus)* Connectez-vous au GUI: https://juju-ws1.lab-linux.com/gui/login



