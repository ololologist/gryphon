from flask import Flask, render_template, send_from_directory

from aws_classes import *

app = Flask(__name__, static_url_path='')

@app.route('/health')
def hello():
    return 'ok'


@app.route('/')
def index():
    cluster_list = list_clusters()
    return render_template('index.html', clusters=cluster_list)


@app.route('/cluster/<cluster_name>/', methods=['GET', 'POST'])
def cluster(cluster_name):
    authorization_data = get_authorization()
    cluster = Cluster(name=cluster_name)
    return render_template('cluster.html', cluster=cluster, auth_data=authorization_data)


@app.route('/task_definitions/', methods=['GET', 'POST'])
def task_definitions():
    authorization_data = get_authorization()
    task_definitions = get_task_def_list()
    return render_template('definitions.html', task_definitions=task_definitions, should_exec=False, auth_data=authorization_data)


@app.route('/static/<path:path>')
def send_staticfles(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run(debug=True)
