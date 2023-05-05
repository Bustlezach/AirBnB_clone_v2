#!/usr/bin/env bash
# Prepare your web servers

sudo apt-get update -y
sudo apt-get install nginx

mkdir -p /data
mkdir -p /data/web_static
mkdir -p /data/web_static/releases
mkdir -p /data/web_static/shared
mkdir -p /data/web_static/releases/test

sudo touch /data/web_static/releases/test/index.html
html_content= "<html>
  <head>
  </head>
  <body>
    Alx School
  </body>
</html>"
echo "$html_content" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sm /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

server= "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /var/www/html;
    index  index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    
    location /redirect_me {
        return 301 https://google.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"
echo "$server" | sudo tee /etc/nginx/sites-available/default


service nginx restart
