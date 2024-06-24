import json
from flask_cors import CORS
from flask_restful import Api, Resource
from flask import Flask, request, jsonify, Response, send_from_directory, abort
from data_converter import DataManager

app = Flask(__name__)
data_manager = DataManager()

app.config['UPLOAD_FOLDER'] = 'C:/Users/Eddy/Desktop/projects/tarot_reader/tarot_api'

@app.route('/collect-csv')
def get_csv():
    return send_from_directory(app.config['UPLOAD_FOLDER'] , path=data_manager.csv_file, as_attachment=False)

@app.route('/collect-data')
def get_data():
    return data_manager.get_json_data()
        
if __name__ == '__main__':
    app.run()