"""
Project: Flask-MasterWorkflowExample
Description: See project readme. 
Notes:
"""
#==============================Imports=======================================
import sys, os

from flask import Flask, render_template, abort, request, session, redirect, url_for
from jinja2.exceptions import TemplateNotFound

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
    if (route == 'login') or (session.get('loggedin') != True):
        if request.method == 'POST':
            try:
                session['loggedin'] = True
                if route == 'login':
                    return render_template("master.html", page2load='home')
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
	app.run(host='',port=8080)
if(__name__ == "__main__"):
	main()
