from flask import Flask
# from flask_migrate import Migrate
# from flask_minify import Minify
# from src.service import create_app

app = Flask(__name__)
UPLOAD_FOLDER = './image'


import src.service.imgProcess.endpoint
# app = create_app()
# Migrate(app)
# Minify(app=app)

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


if __name__ == "__main__":
    app.run()
