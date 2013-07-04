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

Flask comes with the [http://werkzeug.pocoo.org/](Werkzeug server) and [http://jinja.pocoo.org/](Jinja2 templating) which both of them done by [http://lucumr.pocoo.org/projects/](Armin Ronacher).



