# -*- coding: utf-8 -*-
import csv
import json
import logging
import os

from flask import Flask, request, jsonify, redirect
from jinja2 import Environment, PackageLoader

from doc_processor import DocumentProcessor


def setup_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s: '
                               '(%(threadName)-10s) %(message)s')


UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['docx'])

app = Flask('tvshow-scheduler', static_folder='web/static/', static_url_path='/static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def open_file(filename):
    data = []
    with open(filename, 'r') as f:
        iterator = csv.reader(f)
        next(iterator)
        for entry in iterator:
            item = dict()
            item['seq'] = entry[0]
            item['name'] = entry[1].decode('utf-8')
            item['duration'] = entry[2]
            item['plan'] = entry[3]
            data.append(item)
    return data


@app.route('/_get_table')
def get_table():
    file_name = os.path.join(app.config['UPLOAD_FOLDER'], 'data.json')
    data = json.loads(open(file_name, 'r').read())
    for item in data:
        item['duration'] = item['duration']['timeStr']
        item['plan'] = item['plan']['timeStr']

    return jsonify(table=data)


@app.route('/_save_table', methods=['POST'])
def save_table():
    data = request.data
    file_name = os.path.join(app.config['UPLOAD_FOLDER'], 'data.json')
    if os.path.exists(file_name):
        os.remove(file_name)
    with open(file_name, 'a') as f:
        f.write(data)
    return jsonify(result='ok'), 200


@app.route('/shows', methods=['GET', 'POST'])
def home():
    env = Environment(loader=PackageLoader('web'))
    template_index = env.get_template('shows.html')

    file_name = os.path.join(app.config['UPLOAD_FOLDER'], 'data.docx')

    data = dict()

    if request.method == 'GET':
        return template_index.render(data)

    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            f.save(file_name)
            processor = DocumentProcessor()
            data = processor.get_shows(file_name)
            json_file_name = os.path.join(app.config['UPLOAD_FOLDER'], 'data.json')
            if os.path.exists(json_file_name):
                os.remove(json_file_name)
            with open(json_file_name, 'a') as f:
                f.write(data)
            return redirect('/shows')


if __name__ == '__main__':
    setup_logging()
    app.run(host='0.0.0.0', port=8080)

