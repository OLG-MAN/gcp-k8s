FROM debian:stable-slim

# Install Python3 and cgiwrap
RUN apt update \
    && apt install python3 fortune-mod nginx fcgiwrap -y

# Copy nginx cgi config
COPY fcgiwrap.conf /etc/nginx/

# Make dir from python cgi script
RUN mkdir /usr/lib/cgi-bin -p

# Copy cgi python script and add permission
COPY app.py /usr/lib/cgi-bin/
RUN chmod 755 /usr/lib/cgi-bin/app.py

# Copy nginx config 
COPY default /etc/nginx/sites-available/default

# Copy custom index.html
COPY index.html /var/www/html/index.html

# Restart nginx
RUN service nginx restart

# Run nginx container
CMD /etc/init.d/fcgiwrap start && nginx -g 'daemon off;'
 