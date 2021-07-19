from flask import Blueprint, render_template, request, url_for, redirect, flash, jsonify

views = Blueprint('views', __name__)


@views.route('/static', methods=['GET', 'POST'])
def static():
    if request.method == 'POST':
        return redirect(url_for('views.home'))
    return render_template('static.html')

@views.route('/stream', methods=['GET', 'POST'])
def stream():
    if request.method == 'POST':
        return redirect(url_for('views.home'))
    return render_template('stream.html')

@views.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form['strm'] == 'video':
            return redirect(url_for('views.static'))        
        elif request.form['strm'] == 'cam':
            return redirect(url_for('views.stream'))
            
    return render_template('home.html')