Starting with generating ssh keys

```bash
cd ~/.ssh
ssh-keygen -t rsa -C "email@example.com"
# Print it to the terminal
cat ~/.ssh/id_rsa.pub
ssh-add -K id_pub.pub
```

If your hosting provider supports adding ssh keys, add it through their webinterface. This will allow you to ssh to your server machines without typing your password.
Let's install the **vim** and **HTOP** which is the advanced version of the TOP tool

you can also install nginx from the souce with different options enabled

```bash
mkdir downloads
cd downloads
wget http://nginx.org/download/nginx-1.4.2.tar.gz
tar -xzvf nginx-1.4.2.tar.gz
cd nginx-1.4.2
./configure
```


```bash
user@PythonHackers:~# vim /etc/nginx/conf.d/stg.pythonhackers.com
```


```conf
[program:pythonhackers]
killgroup=true
directory=/var/www/stg.pythonhackers.com/src
environment=HOME=/var/www/stg.pythonhackers.com/venv/,
command=/var/www/stg.pythonhackers.com/venv/bin/python flask_app.py
autostart=true
autorestart=true
redirect_stderr=true
stopsignal=INT
```


## Installing PostgreSQL

[Postgres](http://www.postgresql.org/download/linux/ubuntu/) install page is a great start point for installating postgeSQL to your Ubuntu version

```bash
user@PythonHackers:~# apt-get install postgresql-9.1 libpq-dev
Moving configuration file /var/lib/postgresql/9.1/main/postgresql.conf to /etc/postgresql/9.1/main...
Moving configuration file /var/lib/postgresql/9.1/main/pg_hba.conf to /etc/postgresql/9.1/main...
Moving configuration file /var/lib/postgresql/9.1/main/pg_ident.conf to /etc/postgresql/9.1/main...
Configuring postgresql.conf to use port 5432...
```

## Installing Memcache

```bash
user@PythonHackers:~# apt-get install memcached
Unpacking memcached (from .../memcached_1.4.14-0ubuntu1_amd64.deb) ...
Processing triggers for man-db ...
Processing triggers for ureadahead ...
Setting up libevent-2.0-5:amd64 (2.0.19-stable-3) ...
Setting up memcached (1.4.14-0ubuntu1) ...
Starting memcached: memcached.
Processing triggers for libc-bin ...
ldconfig deferred processing now taking place
Processing triggers for ureadahead ...
```

List the available memory on the machine

```bash
free -lmt
```