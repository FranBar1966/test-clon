"""app contollers"""

# Each route must also be added to schema.json:
#
# "validRoutes": [
#     "home",
#     ...
# ],
#
# Since there is a default handler, you can create routes from
# the schema without the need of a contoller here.

import os
from flask import Flask, request, send_from_directory
from constants import STATIC_FOLDER
from schema import Schema
from template import Template
# import pprint

app = Flask(__name__)


@app.route('/<path:route>', methods=['GET', 'POST'])
def catch_all(route):
    """default handle"""

    file_path = os.path.join(STATIC_FOLDER, route)
    if os.path.exists(file_path) and not os.path.isdir(file_path):
        return send_from_directory(STATIC_FOLDER, route)

    schema = Schema(request, route)
    template = Template(schema.get())
    return template.render()

@app.route('/login/<action>', defaults={'route': 'form-login'}, methods=['POST'])
def login(route):
    """route form-login"""
    schema = Schema(request, route)
    schema.schema["data"]["send_form_login"] = 1
    schema.schema["data"]["CONTEXT"]["SESSION"] = "69bdd1e4b4047d8f4e3"
    template = Template(schema.get())
    return template.render()

@app.route('/form-login', defaults={'route': 'form-login'}, methods=['POST'])
def form_login(route):
    """route form-login"""
    schema = Schema(request, route)
    schema.schema["data"]["send_form_login"] = 1
    schema.schema["data"]["CONTEXT"]["SESSION"] = "69bdd1e4b4047d8f4e3"
    template = Template(schema.get())
    return template.render()

@app.route('/', defaults={'route': 'home'}, methods=['GET', 'POST'])
def home(route):
    """route home"""
    schema = Schema(request, route)
    template = Template(schema.get())
    return template.render()


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False)
