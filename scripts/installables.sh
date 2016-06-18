

sudo apt-get install python-pip
sudo add-apt-repository "deb https://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main"
wget --quiet -O - https://postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt-get update
sudo apt-get install postgresql
sudo pip install virtualenv
sudo apt-get build-dep python-psycopg2
sudo apt-get install nginx --yes
sudo apt-get install libpq-dev python-dev --yes
sudo apt-get install postgresql --yes
sudo apt-get install postgis --yes
dpkg-query -l postgis


pip install psycopg2
