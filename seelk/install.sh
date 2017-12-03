sudo apt-get install rabbitmq-server
mkdir ~/.virtualenvs
python3 -m venv ~/.virtualenvs/cryptobot
source ~/.virtualenvs/cryptobot/bin/activate
pip3 install --upgrade pip
pip install -r requirements.txt
export PATH=$PATH:/usr/local/sbin
sudo rabbitmq-server -detached
sudo rabbitmqctl add_user admin admin
sudo rabbitmqctl add_vhost vhost
sudo rabbitmqctl set_permissions -p vhost admin ".*" ".*" ".*"
export SENDGRID_API_KEY='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'
./manage.py makemigrations
./manage.py migrate --run-syncdb
./manage.py crypto_init
celery -A seelk worker --loglevel=info
