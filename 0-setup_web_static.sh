#!/usr/bin/env bash
# Prepare your web servers


sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install nginx -y

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

content="<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

echo "$content" | sudo tee /data/web_static/releases/test/index.html >/dev/null

sudo ln -sf /data/web_static/releases/test /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

sudo printf %s "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By \$HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
        return 301 http://google.com/;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}" | sudo tee /etc/nginx/sites-available/default >/dev/null

sudo service nginx restart

