INSTALLATION FACILE:


Pour une installation facile sur Ubuntu:

Crée et activer un environement python, ou utilisé les commande suivante:
- mkdir ~/.envtest
- python3 -m venv ~/.envtest/cryptobot
- source ~/.envtest/cryptobot/bin/activate

Dans le répertoire seelk écrivé dans un shell

- sh install.sh

Cela comprend l'installation et la configuration de RabbitMQ, l'installation des requirements, l'initialisation du projet, et la mise en place de l’environnement sur un shell.

IMPORTANT:
Pour toute nouvelle ouverture de shell utilisé la commande: -shell.sh (met en place les variable d'environnement)


INSTALATION ETAPE PAR ETAPE:


En cas de problème procédé par étape.

Téléchargé et installé RabbitMQ ici: https://www.rabbitmq.com/download.html

Crée un environnement python:
- mkdir ~/.virtualenvs
- python3 -m venv ~/.virtualenvs/cryptobot
- source ~/.virtualenvs/cryptobot/bin/activate
                            
Installé les modules:
- pip3 install --upgrade pip  (Si besoin)
- pip install -r requirements.txt

Paramétré RabbitMQ:
- sudo rabbitmq-server -detached
- sudo rabbitmqctl add_user admin admin
- sudo rabbitmqctl add_vhost vhost
- sudo rabbitmqctl set_permissions -p vhost admin ".*" ".*" ".*"

Lancer la commande: - sh shell.sh

Lancer Celery: - celery -A seelk worker --loglevel=info


UTILISATION:

Ne pas oublier d'être dans votre environement python. (source ~/.envtest/cryptobot/bin/activate)

Dans un 2éme shell lancé le serveur: 
- sh shell.sh
- ./manage.py runserver
                   
Dans un 3 éme shell lancé les commandes: 
- sh shell.sh
- ./manage.py crypto_init
- ./manage.py run_cryptobot
                                        
MAIL:


N'oublier pas de mettre votre mail pour testé la fonctionnalité du mail, disponibles dans crypto.task ligne 35
    
    
BONUS:


Il est aussi possible d'utilisé d'autre currencie , ainsi que de changé les limites maximum et minimum de déclenchement d'alerte

Étape 1: Crée une régle d'alerte en allant sur le lien suivant http://127.0.0.1:8000/crypto/rules/ (Vous pouvez trouvé toute les currencies disponible avec la commande ./manage.py currencie_list)
Il sera important de nommer la currencie par sont raccourcis, tout les nom de currencie disponible sont visible en utilisant la fonction ./manage.py currencie_list

Étape 2: Il vous suffit simplement de rajouté un argument en lançant la commande run_cryptobot , comme l'exemple suivant:-./manage.py run_cryptobot EUR


DETAIL


Pour accédé au détail des rules , il faut rajouté leur nom après l'url , comme ceci http://127.0.0.1:8000/crypto/rules/EUR/

Pour accédé au détail des alertes, il faut rajouté leur id après l'url, comme ceci http://127.0.0.1:8000/crypto/alerts/1/

Pour accédé au détail des users il faut rajouté leur username après l'url, comme ceci http://127.0.0.1:8000/crypto/users/admin
