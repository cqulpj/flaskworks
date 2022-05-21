#!/usr/bin/python3
#coding=utf-8
import datetime

from flask import Flask, render_template
from flask import request, jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/posts')
@app.route('/contact')
@app.route('/reports')
def index():
    return render_template('index.html')

@app.route('/api/getHomeData', methods=['GET', 'POST'])
def get_home_data():
    if request.method == 'GET':
        ret = {'data' : datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S')}
        print(ret)
        return jsonify(ret)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
