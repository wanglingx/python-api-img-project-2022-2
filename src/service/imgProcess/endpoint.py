import os
from __main__ import app
from flask import request
from werkzeug.utils import secure_filename
from flask_restx import Resource, Api
from src.service.imgProcess.logic import Logic as lg

# from src.service.imgProcess import blueprint

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
class Endpoint:    
    @app.route('/uploadsImg', methods=['POST'])
    def uploadImg():
        file = request.files['file']
        if file.filename == '':
            return ('No image selected for uploading')
        if file and allowed_file(file.filename):
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            # lg.img_process(filename)
            return 'file uploaded successfully'
        
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
