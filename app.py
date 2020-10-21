"""
Project: Flask-MasterWorkflowExample
Description: See project readme. 
Notes:
"""
#==============================Imports=======================================
import sys, os

from flask import Flask, render_template, abort, request, session, redirect, url_for
from jinja2.exceptions import TemplateNotFound
from database.DBAuth import DBAuth


app = Flask(__name__)
app.secret_key = os.urandom(24)

#==============================Routes=======================================
@app.route("/", methods = ['GET'])
def index():
    if (session.get('loggedin') != True):
        return redirect('/login')
    else: 
	    return render_template("master.html")

@app.route("/<route>", methods=['GET', 'POST'])
def page(route):
    if (route == 'signup'):
        if request.method == 'POST':
            try: 
                ## do signup 
                db = DBAuth()
                fname = request.form.get("fname")
                lname = request.form.get("lname")
                username = request.form.get("email")
                password = request.form.get("password")
                password2 = request.form.get("password2")

                if db.checkUserExists(username):
                    return render_template("signup.html", message='User already exists. ')

                if (password == password2):
                    success = db.createUser([username, password])
                else:
                    success = False
                
                if (success):
                    return render_template("master.html", page2load='dashboard')
                else: 
                    return render_template("signup.html", message='Failed to sign up. ')

                ##-- 
            except Exception as err: 
                return render_template("signup.html", message='Failed to sign up. Please try again.')
        else: 
            return render_template("signup.html")
    elif (route == 'login') or (session.get('loggedin') != True):
        if request.method == 'POST':
            try:
                #try login 

                username = request.form.get("email")
                password = request.form.get("password")

                db = DBAuth()
                success = db.authenticate([username, password])

                if (success):
                    session['loggedin'] = True
                    return render_template("master.html", page2load='dashboard')
                else: 
                    return render_template("login.html", message="Failed to login. ")
            except Exception as err:
                #'An error occurred processing the form. Please try again later. '
                return render_template("login.html", message=err)
        else: 
            return render_template("login.html")

    if route == 'logout':
        session.pop('loggedin', None)
        return redirect('/login')

    return render_template("master.html", page2load=route)


@app.route("/page/<route>")
def half(route):
    try:
        return render_template(route + ".html")
    except TemplateNotFound:
        abort(404) 

@app.route("/modal/<route>")
def modal(route):
    try:
        return render_template('/modal/' + route + ".html")
    except TemplateNotFound:
        abort(404) 
    
@app.route("/forms/<form>", methods = ["POST"])
def forms(form):
    try:
        raise ValueError("It didnt work. ")
    except:
        #'An error occurred processing the form. Please try again later. '
        return 'Forms are not currently set up on the server. '

@app.errorhandler(404)
def not_found(e):
    return render_template("errors/404.html") 

#==========================Main========================================

def main():
	app.run(host='localhost',port=8080)
if(__name__ == "__main__"):
	main()
