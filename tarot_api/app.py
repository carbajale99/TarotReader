import base64
import io
import json
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from flask import Flask, request, jsonify, Response, send_from_directory, abort
from data_converter import DataManager
from PIL import Image


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
data_manager = DataManager()

app.config['UPLOAD_FOLDER'] = 'C:/Users/Eddy/Desktop/projects/tarot_reader/tarot_api'

@app.route('/collect-csv')
@cross_origin()
def get_csv():
    return send_from_directory(app.config['UPLOAD_FOLDER'] , path=data_manager.csv_file, as_attachment=False)

@app.route('/collect-data')
@cross_origin()
def get_data():
    return data_manager.get_json_data()

@app.route('/get-card-img')
@cross_origin()
def get_img():
    
    img_name = request.args['img']
    
    img_path = app.config['UPLOAD_FOLDER'] + '/card_imgs/' + img_name
    
    with open(img_path, "rb") as img_file:
        img_string =  base64.b64encode(img_file.read()).decode("utf-8")
    
    return jsonify({
                'msg': 'success', 
                'img': img_string
           }) 
        
if __name__ == '__main__':
    app.run()