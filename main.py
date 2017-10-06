from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup.html')

@app.route("/", methods=['POST'])
def validate_input():
    
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    email_error = ''

    if username == '':
        username_error = "Please enter a username"
    elif ' ' in username:
        username_error = "Username cannot contain spaces"
    elif len(username) < 3 or len(username) > 20:
        username_error = "Username must be between 3 & 20 characters"

    if password == '' or verify_password == '':
        password_error = "Please enter a password & verify it"
    elif password != verify_password:
        password_error = "Password & Verify password fields MUST match"
    elif ' ' in password:
        password_error = "Password cannot contain spaces"
    elif len(password) < 3 or len(password) > 20:
        password_error = "Password must be between 3 and 20 characters"

    if email != '':
        if ' ' in email:
            email_error = "Email cannot contain spaces"
        elif len(email) < 3 or len(email) > 20:
            email_error = "Email must be between 3 and 20 characters"
        elif email.count('.') != 1 or email.count('@') != 1:
            email_error = "Email must contain a single '.' & a single '@'"
    if not username_error and not password_error and not email_error:
        return redirect('/welcome?username={0}'.format(username))
    else:
        return render_template('signup.html',
            username_error =username_error,
            password_error = password_error,
            email_error = email_error,
            username = username,
            email = email)

@app.route('/welcome')
def welcome_user():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)
app.run()
        
    

