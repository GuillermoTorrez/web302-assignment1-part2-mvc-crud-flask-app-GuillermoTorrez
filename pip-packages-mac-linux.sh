echo "Upgrade PIP to the latest version"
sudo python -m pip3 install --upgrade pip --user

echo "Install virtualenv"
sudo pip3 install virtualenv --user

echo "Install virtualenvwrapper"
sudo pip3 install virtualenvwrapper --user

echo "Make an environment"
mkvirtualenv myappenv

echo "Install Flask and Flask WTF"
sudo pip3 install Flask-WTF
sudo pip3 show --files Flask-WTF

echo "Install MySQL Connector"
sudo pip3 install mysql-connector
sudo pip3 show --files mysql-connector

sudo pip3 freeze > requirements.txt
