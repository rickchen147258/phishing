Flask
===

###### tags: `Study Group`

## Install

- `pip install flask` to install

## Set the flask app

- ==Windows== system: type `set FLASK_APP={code.py}` in cmd

- ==linux or mac== system: type `export FLASK_APP={code.py}` in terminal
- For example:
    ![](https://i.imgur.com/S2QEykq.png)

---

## Functionality of flask

<em>python backend</em>

- example: application.py
```python
 from flask import Flask
 
 app = Flask(__name__)
 
 @app.route("/")
 def index():
     return "Hello, world!"
     
 @app.route("/david")
 def david():
     return "Hello, David!"
```

- run flask on terminal: `flask run`
    ![](https://i.imgur.com/bwiYl12.png)

- result
    ![](https://i.imgur.com/ocWwGFF.png)

- more general method
```python
 from flask import Flask
 
 app = Flask(__name__)
 
 @app.route("/")
 def index():
     return "Hello, world!"
     
 @app.route("/<string:name>")
 def hello(name):
     name = name.capitalize()
     return f"<h1>Hello, {name}!</h1>"
```

---

## render_template

- example
```python
# application.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, world!"
    return render_template("index.html", headline=headline)
```

- `index.html` is under the `templates` folder

```htmlmixed=
<html>
    <head>
        <title>My Website!</title>
    </head>
    <body>
        <h1>{{ headline }}</h1>
    </body>
</html>
```

---

## jinja2

<em> jinja2 is the method to pass parameter from application.py to html during render process.</em>

### Syntax of jinja2
- syntax for condition
```htmlmixed=if
<body>
    {% if variable %}
        <h1>...</h1>
    {% else %}
        <h1>...</h1>
    {% endif %}
</body>
```

- syntax for loop
```htmlmixed=loop
<ul>
    <!-- names is a list -->
    {% for name in names %}
        <li>{{ name }}</li>
    {% endfor %}
</ul>
```

- syntax for link
```htmlmixed=link
...
<a href="{{ url_for('function_name') }}">Text</a>
...
```

```python
@app.route("/function_name")
def function_name():
    return("test.html")
```

---

## template inheritance

- use a template and every page is inheritate the template

```htmlmixed=inheritance
<!-- layout.html -->
<body>
    <h1>{% block heading %}{% endblock %}</h1>
    {% block body %}
    {% endblock %}
</body>
```

```htmlmixed=index.html
<!-- index.html -->
{% extends "layout.html" %}

{% block heading %}
    First Page
{% endblock %}

{% block body %}
    <p>...</p>
{% endblock %}
```

```htmlmixed=index.html
<!-- second.html -->
{% extends "layout.html" %}

{% block heading %}
    Second Page
{% endblock %}

{% block body %}
    <p>...</p>
{% endblock %}
```

## form

- index.html
```htmlmixed=index.html
{% block body %}
<form action="{{ url_for('hello') }}" method="post">
    <input type="text" name="name" placeholder="Enter Your Name">
    <button>Submit</button>
</form>
{% endblock %}
```

- application.py
```python
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", method=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)
```

---

## Sessions

```python
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SEESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET","POST"])
def index():
    if session.get["notes"] is None:
        session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("index.html", notes=session["notes"])
```

---
