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

@app.route('/problem/<pid>',methods=['GET','POST'])
def Problem(pid):
	if request.method == 'GET':
		return sites.problem.page.Run(int(pid))
	else:
		rid = sites.newsubmit.page.Submit(int(pid),request.form)
		return redirect('/record/%d'%rid)

@app.route('/status')
def Status():
	return sites.status.page.Run()

@app.route('/help')
def Help():
	return sites.help.page.Run()

@app.route('/record/<int:rid>')
def Record(rid):
	return sites.record.page.Run(rid)
