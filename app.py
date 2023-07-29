# app.py
from flask import Flask, jsonify
from werkzeug.utils import secure_filename
from os import listdir, remove, path

app = Flask(__name__)

# json 데이터를 리턴함 
# 이미지 경로를 전달할 예정
@app.route('/api/flask', methods=['GET'])
def flask_data():
    data = {'path': './images/node.png'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='https://port-0-hairthon-api-server-rt92alkjpc0lh.sel4.cloudtype.app/')
