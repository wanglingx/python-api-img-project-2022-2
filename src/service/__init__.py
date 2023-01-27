from flask import Flask
from importlib import import_module

def imgProcess_blueprints(app):
    #for module_name in ('imgProcess'):
        module = import_module('/src/service/imgProcess/endpoint.py')
        app.imgProcess_blueprints(module.blueprint) 


def create_app():
    app = Flask(__name__)
    imgProcess_blueprints(app)
    return app
