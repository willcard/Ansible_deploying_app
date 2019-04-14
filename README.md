# Ansible Deploying App


## Préparer les machines vagrant 

* ``` cd ansible ```
* ``` vagrant up ```
* ``` ssh-keygen -R 192.168.201.12 && ssh-keygen -R 192.168.201.11 && ssh-keygen -R 192.168.201.10 ```
``` && ssh-keygen -R 192.168.201.13 && ssh-keygen -R 192.168.201.14 ```

## Executer le playbook

``` ansible-playbook --inventory-file inventories/app deploy-app.yml ```

## Observer le résultat
* ``` 192.168.201.10 ``` pour obtenir l'application sur un navigateur web.
* ``` 192.168.201.10:8080/stats ``` (**login:** _bonjour_ / **mdp:** _aurevoir_) pour afficher les statistiques 
 de connexion sur chaque app.
