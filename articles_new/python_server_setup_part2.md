

In [Part 1](http://pythonarticles.com/python_server_setup_part1.html) we covered up, installing the bare minimums to get starting
with. At last, we setip our setup with <code>Nginx -> Supervisor -> uWSGI -> Python Flask</code> via port forwarding.

- Nginx -> Supervisor -> uWSGI -> Python Flask [via unix socket]

## Nginx - uWSGI via Sockets

uWSGI master process for our program will take care of all the socket communication between Nginx and forward the
request into python process(es).


```conf
#--socket=/tmp/stg.pythonhackers.com.sock
#-C666
uwsgi -s /tmp/multicdn.sock -H /var/www/stg.pythonhackers.com/venv/ -w spilmulticdn.wsgi -M -p 4 -C 666
```