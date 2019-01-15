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

@app.route('/problem/<problemid>',methods=['GET','POST'])
def Problem(problemid):
	if request.method == 'GET':
		return sites.problem.page.Run(int(problemid))
	else:
		runid = sites.newsubmit.page.Submit(int(problemid),request.form)
		return redirect('/record/%d'%runid)

@app.route('/status')
def Status():
	return sites.status.page.Run()

@app.route('/help')
def Help():
	return sites.help.page.Run()

@app.route('/record/<int:runid>')
def Record(runid):
	return sites.record.page.Run(runid)

@app.route('/problemadd',methods=['GET','POST'])
def Problemadd():
	if request.method == 'GET':
		return sites.problemadd.page.Run()
	else:
		id = sites.problemadd.page.Submit(request.form)
		return redirect('/problem/%d' % id)
