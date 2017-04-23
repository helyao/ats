from . import main
from flask import render_template

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/loadctl_base')
def loadctl_base():
    return render_template('control1.html')

@main.route('/loadctl_debug')
def loadctl_debug():
    return render_template('control2.html')

@main.route('/equpctl_base')
def equpctl_base():
    return render_template('control3.html')

@main.route('/history_equip')
def history_equip():
    return render_template('history1.html')

@main.route('/history_user')
def history_user():
    return render_template('history2.html')

@main.route('/data_table')
def data_table():
    return render_template('data1.html')

@main.route('/data_distribution')
def data_distribution():
    return render_template('data2.html')

@main.route('/data_compare')
def data_compare():
    return render_template('data3.html')

@main.route('/bug_list')
def bug_list():
    return render_template('bug1.html')

@main.route('/bug_distribution')
def bug_distribution():
    return render_template('bug2.html')

@main.route('/manage_user')
def manage_user():
    return render_template('manage1.html')

@main.route('/manage_map')
def manage_map():
    return render_template('manage2.html')

@main.route('/manage_load')
def manage_load():
    return render_template('manage3.html')

@main.route('/manage_equip')
def manage_equip():
    return render_template('manage4.html')

@main.route('/message')
def message():
    return render_template('message.html')