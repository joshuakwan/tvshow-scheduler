# -*- coding: utf-8 -*-
import csv
import logging
import os

from flask import Flask, request, jsonify, redirect
from jinja2 import Environment, PackageLoader

from display_time import DisplayTime
from shows import Shows


def setup_logging():
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(levelname)s %(name)s: '
                               '(%(threadName)-10s) %(message)s')


UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = set(['csv'])

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
    time_str = request.args.get('time')
    time_now = DisplayTime(time_str)
    file_name = os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv')
    with open(file_name, 'r') as f:
        iterator = csv.reader(f)
        next(iterator)
        shows_data = [entry for entry in iterator]
        global_shows = Shows(shows_data)
    table = global_shows.get_shows_table(time_now)
    return jsonify(table=table)


@app.route('/shows', methods=['GET', 'POST'])
def home():
    env = Environment(loader=PackageLoader('web'))
    template_index = env.get_template('shows.html')

    file_name = os.path.join(app.config['UPLOAD_FOLDER'], 'data.csv')

    data = dict()

    if os.path.exists(file_name):
        data['shows'] = open_file(file_name)

    if request.method == 'GET':
        return template_index.render(data)

    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            f.save(file_name)
            return redirect('/shows')


if __name__ == '__main__':
    setup_logging()
    app.run(host='0.0.0.0', port=8080)
