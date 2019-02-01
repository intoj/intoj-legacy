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

@app.route('/problem/<int:problemid>',methods=['GET','POST'])
def Problem(problemid):
	if request.method == 'GET':
		return sites.problem.page.Run(int(problemid))
	else:
		print(request.form)
		runid = sites.newsubmit.page.Submit(int(problemid),request.form)
		return redirect('/record/%d'%runid)

@app.route('/status')
def Status():
	return sites.status.page.Run()

@app.route('/help')
def Help():
	return sites.help.page.Run()

@app.route('/record/<int:runid>',methods=['GET','POST'])
def Record(runid):
	if request.method == 'GET':
		return sites.record.page.Run(runid)
	else:
		is_success = sites.newsubmit.page.Rejudge(runid)
		if not is_success: return render_template('error.html',message="提交记录R%d没找着!\n可能是因为编号不对."%runid)
		else: return redirect('/record/%d'%runid)

@app.route('/problemadd',methods=['GET','POST'])
def Problemadd():
	if request.method == 'GET':
		return sites.problemadd.page.Run()
	else:
		id = sites.problemadd.page.Submit(request.form)
		return redirect('/problem/%d' % id)

@app.route('/problem/<int:problemid>/edit',methods=['GET','POST'])
def Problemedit(problemid):
	if request.method == 'GET':
		return sites.problemedit.page.Run(problemid)
	else:
		newid = sites.problemedit.page.Change(problemid,request.form)
		return redirect('/problem/%d' % newid)

@app.route('/problem/<int:problemid>/delete',methods=['GET'])
def Problemdel(problemid):
	return sites.problemdel.page.Deleteproblem(problemid)
