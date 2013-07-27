
# Server setup

This article describes the server setup for your python project. The assumption is that
you will use **Ubuntu**. Probably depending on the distribution, you might use other package managers ;

Red Hat EL or SL => yum
CentOS => yum
Arch Linux => pacman
Fedora => yum
Debian => dpkg

Starting with generating ssh keys

```bash
cd ~/.ssh
ssh-keygen -t rsa -C "email@example.com"
# Print it to the terminal
cat ~/.ssh/id_rsa.pub
ssh-add -K id_pub.pub
```

If your hosting provider supports adding ssh keys, add it through their webinterface.

This will allow you to ssh to your server machines without typing your password.

Let's install the HTOP tool which is the advanced version of the TOP tool

```bash
sudo apt-get install htop vim
```

List the available memory on the machine

```bash
free -lmt
```

```bash
apt-get update
apt-get install make python-dev build-essential
```

Lets check which python version we are running. I have Python 2.7.3 installed on default on 12.10 Ubuntu 64bit

```bash
user@PythonHackers:~# python
Python 2.7.3 (default, Apr 10 2013, 05:13:16)
[GCC 4.7.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

## Installing VirtualEnv

```bash
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz
tar xvfz virtualenv-1.9.1.tar.gz
cd virtualenv-1.9.1
sudo python setup.py install
```

## Install Supervisor

<code> apt-get install supervisor</code> will get the job done...

```bash
user@PythonHackers:~# apt-get install supervisor
Setting up supervisor (3.0a8-1.1) ...
Starting supervisor: supervisord.
Processing triggers for python-support ...
Processing triggers for ureadahead ...
user@PythonHackers:~# service supervisor status
 is running
```

Let's check if we have Nginx in our system. The answer will be probably **No**

```bash
user@PythonHackers:~# ps aux | grep nginx
root      1376  0.0  0.0   9388   892 pts/0    S+   20:48   0:00 grep --color=auto nginx
```

Only the <code>grep</code> itsself. Nginx is not installed. Let's install it. <code>apt-get install nginx</code>

```bash
user@PythonHackers:~# sudo apt-get install nginx
Processing triggers for libc-bin ...
ldconfig deferred processing now taking place
user@PythonHackers:~# sudo service nginx start
Starting nginx: nginx.
user@PythonHackers:~# service nginx status
 * nginx is running
```

After the service is started and verified that the nginx is up and running let's try our nginx and go to <code>http://stg.pythonhackers.com</code>

Let's check the nginx log if our request

```bash
user@PythonHackers:~# tail -f /var/log/nginx/access.log
XX.XXX.XX.XX - - [26/Jul/2013:21:13:28 +0000] "GET / HTTP/1.1" 200 133 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36"
XX.XXX.XX.XX - - [26/Jul/2013:21:13:29 +0000] "GET /favicon.ico HTTP/1.1" 200 133 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36"
```

You will see that <code>XX.XXX.XX.XX</code> will actually contain your IP address. On the browser, you should see
that the Nginx default page is rendered.

We have add our pythonhackers configuration to Nginx.

```bash
user@PythonHackers:~# vim /etc/nginx/nginx.conf
```

Press <code>:71</code> you will see that all the conf files underneath the conf.d folder will be included. This is
also the preferred/suggested way of adding configurations for websites(virtualhosts).

```
Line 71: include /etc/nginx/conf.d/*.conf;
Line 72: include /etc/nginx/sites-enabled/*;
```

Let's create a new virtualhost configuration file for nginx

```bash
user@PythonHackers:~# vim /etc/nginx/conf.d/stg.pythonhackers.com
```

```conf
server {
    # virtualhost
    server_name    stg.pythonhackers.com;
    #include     conf/defaults.conf ;

    # serve static files from webroot
    location /static/ {
        alias /var/www/pythonhackers.com/src/;
    }

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/tmp/stg.pythonhackers.sock;
        access_log /var/log/nginx/stg.pythonhackers.com/access.log;
    }
}
```

```bash
user@PythonHackers:~# service nginx reload
Reloading nginx configuration: nginx.
```


You will start to get 502 - Bad Gateway

```bash
user@PythonHackers:/var/log/nginx/stg.pythonhackers.com# less access.log
```

```
XX.XXX.XX.XX - - [26/Jul/2013:22:09:19 +0000] "GET / HTTP/1.1" 502 574 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36"
```

and the error.log will say

```
2013/07/26 22:09:19 [crit] 9461#0: *1 connect() to unix:/tmp/stg.pythonhackers.sock failed (2: No such file or directory) while connecting to upstream, client: XX.XXX.XX.XX, server: stg.pythonhackers.com, request: "GET / HTTP/1.1", upstream: "uwsgi://unix:/tmp/stg.pythonhackers.sock:", host: "stg.pythonhackers.com"
```

Allright, now nginx tried to open a socket connection to our specified socket <code>/tmp/stg.pythonhackers.com.sock</code>
but failed, so we received a 502. <code>uwsgi_pass unix:/tmp/stg.pythonhackers.sock;</code> contains the nginx directive.

Let's step back, and change this into a port forwarding operation.

```
location / {
    proxy_pass  http://127.0.0.1:5000/;
    proxy_set_header    Host    $host;
    proxy_set_header    X-Real-IP   $remote_addr;
    }
```

This will tell the nginx to forward the request to the post 5000. Comment out the previous <code>location /</code>
and replace with the <code>proxy_pass</code> block.

Python has a builtin http server module <code>python -m SimpleHTTPServer port_number</code>. Go to stg.pythonhackers.com
and you will see the directory listing

```bash
user@PythonHackers:/var/log/nginx/stg.pythonhackers.com# python -m SimpleHTTPServer 5000
Serving HTTP on 0.0.0.0 port 5000 ...
127.0.0.1 - - [26/Jul/2013 22:28:49] "GET / HTTP/1.0" 200 -
```

The access log will also say

```
XX.XXX.XX.XX - - [26/Jul/2013:22:31:09 +0000] "GET / HTTP/1.1" 200 183 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.71 Safari/537.36"
```

```bash
user@PythonHackers:# mkdir -p /var/www/stg.pythonhackers.com/src
user@PythonHackers:# cd /var/www/stg.pythonhackers.com/src
user@PythonHackers:/var/www/stg.pythonhackers.com/src# vim app.py
```

and paste the following code


```python
import SimpleHTTPServer
import SocketServer

PORT = 5000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()
```

and go to stg.pythonhackers.com

```bash
user@PythonHackers:/var/www/stg.pythonhackers.com/src# python app.py
serving at port 5000
# ONCE THE REQUEST IS Arrived!!
127.0.0.1 - - [26/Jul/2013 22:35:16] "GET / HTTP/1.0" 200 -
127.0.0.1 - - [26/Jul/2013 22:35:19] "GET /app.py HTTP/1.0" 200 -
```

Congrulatulations, your dummy app is served through port 5000...

[Supervisor](http://supervisord.org) is our tool to manage our required processes and it's not bound to the Python
only processes as well.

```bash
user@PythonHackers:# cd /etc/supervisor/conf.d/
user@@PythonHackers:/etc/supervisor/conf.d# vim stg.pythonhackers.com.conf
```

paste the following configuration

```conf
[program:pythonhackers] # Name of our app, this will help us to manage the status of the app via supervisorctl
killgroup=true
directory=/var/www/stg.pythonhackers.com/src
environment=HOME=/var/www/stg.pythonhackers.com/src/,
command=/var/www/stg.pythonhackers.com/src/python app.py
autostart=true
autorestart=true
redirect_stderr=true
stopsignal=INT
```

Lets kick off supervisor again. Then <code>supervisorctl</code> will help us manage our processes.

```bash
user@PythonHackers:/etc/supervisor/conf.d# service supervisor restart
user@PythonHackers:/etc/supervisor/conf.d# supervisorctl
pythonhackers                    RUNNING    pid 9633, uptime 0:00:04
supervisor> status
supervisor> help

default commands (type help <topic>):
=====================================
add    clear  fg        open  quit    remove  restart   start   stop  update
avail  exit   maintail  pid   reload  reread  shutdown  status  tail  version

supervisor> stop pythonhackers
pythonhackers: stopped
supervisor> status
pythonhackers                    STOPPED    Jul 26 10:51 PM
supervisor> start pythonhackers
pythonhackers: started
supervisor> reread
pythonhackers: changed
supervisor> stop pythonhackers
pythonhackers: stop
supervisor> start pythonhackers
pythonhackers: started
supervisor> status
pythonhackers                    RUNNING    pid 9840, uptime 0:00:04

```

<code>reread</code> command looks for configuration changes. Consult supervisor documentation for more detail.

From command line you can also start/stop your application via <code> supervisorctl restart pythonhackers </code>

## VirtualEnv

The next step will be installing Flask, and starting to serve our Flask application through port 5000.

```bash
root@PythonHackers:/var/www/stg.pythonhackers.com/src# cd ../
root@PythonHackers:/var/www/stg.pythonhackers.com# ls
src
root@PythonHackers:/var/www/stg.pythonhackers.com# virtualenv venv
New python executable in venv/bin/python
Installing setuptools............done.
Installing pip...............done.
root@PythonHackers:/var/www/stg.pythonhackers.com# source venv/bin/activate
(venv)root@PythonHackers:/var/www/stg.pythonhackers.com# pip install Flask
Downloading/unpacking Flask
  Downloading Flask-0.10.1.tar.gz (544kB): 544kB downloaded
  Running setup.py egg_info for package Flask
  # After a BIT OF LINES
 Successfully installed Flask Werkzeug Jinja2 itsdangerous markupsafe
Cleaning up...
(venv)root@PythonHackers:/var/www/stg.pythonhackers.com# pip freeze
Flask==0.10.1
Jinja2==2.7
MarkupSafe==0.18
Werkzeug==0.9.3
argparse==1.2.1
itsdangerous==0.22
wsgiref==0.1.2
(venv)root@PythonHackers:/var/www/stg.pythonhackers.com# pip freeze > requirements.txt
(venv)root@PythonHackers:/var/www/stg.pythonhackers.com# cat requirements.txt
Flask==0.10.1
Jinja2==2.7
MarkupSafe==0.18
Werkzeug==0.9.3
argparse==1.2.1
itsdangerous==0.22
wsgiref==0.1.2
```

We will use this structure later.

## Flask

Follow the bash command to create the flask code;

```bash
(venv)root@PythonHackers:/var/www/stg.pythonhackers.com/src# vim flask_app.py
```

Paste the following lines to your <code>flask_app.py</code>. That is all you need in Flask to start everything ( **Cough Cough Django** )

```python
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True,port=5000)
```

lets fire up the flask engine..

```bash
(venv)root@PythonHackers:/var/www/stg.pythonhackers.com/src# python flask_app.py
 * Running on http://127.0.0.1:5000/
 * Restarting with reloader
```

It's time to update our supervisor configuration file to serve our most basic Flask server...

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

set our virtualenvironment home directory <code>/var/www/stg.pythonhackers.com/venv/</code> and also change the command to run <code>/var/www/stg.pythonhackers.com/venv/bin/python</code> with <code>flask_app.py</code> argument.

```bash
user@PythonHackers:~# /etc/init.d/supervisor stop
user@PythonHackers:~# /etc/init.d/supervisor start
```

Now our Flask app is running via supervisord.

## uWSGI

Web Server Gateway Interface

The internet is full of slow connections and in our setup right now, Flask needs to deal with that. This is not a good way to 
continue our development, and also we are running a single instance of our application. **Not good**!

Let's introduce the awesomeness of uWSGI which will take care a lot for us.

```bash
user@PythonHackers:~# source /var/www/stg.pythonhackers.com/venv/bin/activate
pip install http://projects.unbit.it/downloads/uwsgi-lts.tar.gz
(venv)root@PythonHackers:~# pip install [](http://projects.unbit.it/downloads/uwsgi-lts.tar.gz)
```

```bash
(venv)root@PythonHackers:/var/www/stg.pythonhackers.com/src# /var/www/stg.pythonhackers.com/venv/bin/uwsgi  -H /var/www/stg.pythonhackers.com/venv/ -w flask_app:app -M -p 1 --http :5000
*** Starting uWSGI 1.4.9 (64bit) on [Sat Jul 27 01:56:06 2013] ***
compiled with version: 4.7.2 on 27 July 2013 01:52:19
os: Linux-3.5.0-17-generic #28-Ubuntu SMP Tue Oct 9 19:31:23 UTC 2012
nodename: PythonHackers
machine: x86_64
clock source: unix
detected number of CPU cores: 2
current working directory: /var/www/stg.pythonhackers.com/src
detected binary path: /var/www/stg.pythonhackers.com/venv/bin/uwsgi
your processes number limit is 31578
your memory page size is 4096 bytes
detected max file descriptor number: 1024
lock engine: pthread robust mutexes
uWSGI http bound on :5000 fd 4
uwsgi socket 0 bound to TCP address 127.0.0.1:33661 (port auto-assigned) fd 3
Python version: 2.7.3 (default, Apr 10 2013, 05:16:12)  [GCC 4.7.2]
Set PythonHome to /var/www/stg.pythonhackers.com/venv/
*** Python threads support is disabled. You can enable it with --enable-threads ***
Python main interpreter initialized at 0x22a3910
your server socket listen backlog is limited to 100 connections
mapped 144848 bytes (141 KB) for 1 cores
*** Operational MODE: single process ***
WSGI app 0 (mountpoint='') ready in 1 seconds on interpreter 0x22a3910 pid: 13974 (default app)
*** uWSGI is running in multiple interpreter mode ***
spawned uWSGI master process (pid: 13974)
spawned uWSGI worker 1 (pid: 13979, cores: 1)
spawned uWSGI http 1 (pid: 13980)
[pid: 13979|app: 0|req: 1/1] 127.0.0.1 () {40 vars in 924 bytes} [Sat Jul 27 01:56:10 2013] GET / => generated 38 bytes in 3 msecs (HTTP/1.0 200) 2 headers in 79 bytes (1 switches on core 0)
```

So what do we know ? 

- Set the correct directory
- Since we are still communicating via port use <code> --http :5000</code> syntax
- Set the Environment Home directory <code>-H /var/www/stg.pythonhackers.com/venv/ </code>
- Set process to 1 <code> -p 1 </code>
- Set to master process <code> -m </code>
- Set the worker <code>-w flask_app:app</code> There is a worker inside the <code>flask_app</code> py file and in that file use the variable called <code>app</code>


```conf
command=uwsgi
            --master
            --http :5000
            --virtualenv=/var/www/stg.pythonhackers.com/venv/
            --workers=4
            --chdir=/var/www/stg.pythonhackers.com/src
```

more settings

```conf
#--socket=/tmp/stg.pythonhackers.com.sock
#-C666
uwsgi -s /tmp/multicdn.sock -H /var/www/stg.pythonhackers.com/venv/ -w spilmulticdn.wsgi -M -p 4 -C 666
```
