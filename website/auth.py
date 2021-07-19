from flask import Blueprint, render_template, request, flash, redirect, url_for

auth = Blueprint('auth', __name__)


@auth.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        
        if password == '123':
            flash('Logged in successfully!', category='success')
            return redirect(url_for('views.home'))
        else:
            flash('Incorrect password, try again.', category='error')


    return render_template('login.html')

@auth.route('/logout')
def logout():
    return redirect(url_for('auth.login'))



