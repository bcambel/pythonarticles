Flask is the minimalistic simple Web Framework for Python. Want to start serving page immediately ? 

```
mkdir flask101
cd flask101
virtualenv .
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

```shell
python server.py
# * Running on http://127.0.0.1:5000/
```

Navigate to ```http://localhost:5000/``` and you will get the Hello World message.

Flask comes with the [Werkzeug server](http://werkzeug.pocoo.org/) and [Jinja2 templating](http://jinja.pocoo.org/) which both of them done by [Armin Ronacher](http://lucumr.pocoo.org/projects/).



