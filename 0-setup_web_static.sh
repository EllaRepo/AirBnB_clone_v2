#!/usr/bin/env bash
# sets up web servers for the deployment of web_static
# Install Nginx server
apt-get -y update
apt-get -y install nginx
service nginx start
# Create folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
# Create HTML file
echo "Hello Web Server!" > /data/web_static/releases/test/index.html
# Create symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current
# Change ownership of /data/
chown -R ubuntu:ubuntu /data/
# configuring Nginx
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default
service nginx restart
# Always exit successfully
exit 0
