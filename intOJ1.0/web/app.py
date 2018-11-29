#export FLASK_ENV=development
from flask import *
import sys,time
import sites
app = Flask(__name__)

@app.route('/')
def Home():
	return sites.home.page.Run()

@app.route('/problems')
def Problems():
	return sites.problems.page.Run()

@app.route('/status')
def Status():
	return sites.status.page.Run()

@app.route('/help')
def Help():
	return sites.help.page.Run()
