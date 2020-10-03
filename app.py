"""
Project: Flask-MasterWorkflowExample
Description: See project readme. 
Notes:
"""
#==============================Imports=======================================
import sys

from flask import Flask, render_template, abort
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

#==============================Routes=======================================
@app.route("/", methods = ["GET"])
def index():
	return render_template("master.html")

@app.route("/<route>")
def page(route):
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
