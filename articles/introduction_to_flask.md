[Flask](http://flask.pocoo.org/) is the minimalistic simple Web Framework for Python. 
Want to start serving page immediately ? 


```bash
mkdir flask101
cd flask101
virtualenv venv
# Not installed virtualenv ? 
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz
tar xvfz virtualenv-1.9.1.tar.gz
cd virtualenv-1.9.1
sudo python setup.py install
# now activate the virtualenv
source venv/bin/activate
pip install Flask
touch server.py
vim server.py
```

Save the following 

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

```bash

python server.py
* Running on http://127.0.0.1:5000/

```

Navigate to ```http://localhost:5000/``` and you will get the Hello World message.

Flask comes with the [Werkzeug server](http://werkzeug.pocoo.org/) and [Jinja2 templating](http://jinja.pocoo.org/) which both of them done by [Armin Ronacher](http://lucumr.pocoo.org/projects/).

Templating
-----------------

Create a folder named ```templates``` and lets add a basic HTML page under the templates folder.
```html
<!DOCTYPE html>
<html>
    <body>
        Hello world from flask
    </body>
</html>
```


```python
from flask import Flask, render_template
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
template_folder = os.path.join(current_dir, 'templates')
app = Flask(__name__, template_folder=template_folder)

@app.route("/")
def hello():
    #return "Hello World!"
    return render_template("hello.html")
    

if __name__ == "__main__":
    app.run(debug=True)
```

How to send a parameter to Flask template ?
--------------------------------------------

Adding our parameter to the ```hello.html```

```html
<!DOCTYPE html>
<html>
    <body>
        Hello world from flask! My name is {{name}}
    </body>
</html>
```

As you see, <code>{{name}}</code> added to our HTML file. All we need to do, add ```name``` as a named parameter to our
<code>render_template</code>

```python
@app.route("/")
def hello():
    #return "Hello World!"
    return render_template("hello.html", name='Bahadir')
```

How to serve static files from Flask ? 
-------------------------------------

Our previous code was 

```python
if __name__ == "__main__":
    app.run(debug=True)
```

We would like to serve our static files in our development environment. Let's create a static folder under our project
to put <code>JavaScript</code>, <code>CSS</code>, <code>Images</code>

```bash
mkdir static && cd static
mkdir img && mkdir js && mkdir css
```

```python
if __name__ == "__main__":
    if app.debug:
       from werkzeug import SharedDataMiddleware

       app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static': static_folder
        })
    app.run(debug=True, use_debugger=True, use_reloader=True)

```

Set <code>use_reloader=True</code> to restart flask server whenever a Python file changes. Very handy!
