#export FLASK_ENV=development
from flask import *
import sys,time
import sites
app = Flask(__name__)

@app.route('/')
def Home():
	return sites.home.page.Run()

@app.route('/problemlist')
def Problemlist():
	return sites.problemlist.page.Run()

@app.route('/problem/<pid>')
def Problem(pid):
	return sites.problem.page.Run(int(pid))

@app.route('/status')
def Status():
	return sites.status.page.Run()

@app.route('/help')
def Help():
	return sites.help.page.Run()
