#coding:utf-8
from flask import *
import sys,os,time,random
import hashlib,re
workpath = os.path.dirname(os.path.abspath(sys.argv[1]))
sitespath = os.path.join(workpath,'sites')
if sitespath not in sys.path:
	sys.path.insert(0,sitespath)
import sites

app = Flask(__name__)

app.add_template_global(sites.modules.Score_Color,'Score_Color')
app.add_template_global(sites.modules.tostatus,'tostatus')
app.add_template_global(sites.modules.shortstatus,'shortstatus')
app.add_template_global(sites.modules.statusicon,'statusicon')
app.add_template_global(sites.modules.statuscolor,'statuscolor')
app.add_template_global(sites.modules.Email_Hash,'Email_Hash')
app.add_template_global(sites.modules.Toint,'Toint')
app.add_template_global(sites.modules.Judge_Status,'Judge_Status')
app.add_template_global(sites.modules.Current_User_Privilege,'Current_User_Privilege')
app.add_template_global(sites.modules.Is_Loggedin,'Is_Loggedin')
app.add_template_global(sites.db.User_Privilege,'User_Privilege')
app.add_template_global(sites.db.Read_Problem,'Read_Problem')
app.add_template_global(sites.db.Read_User_Byname,'Read_User_Byname')

@app.route('/error/<message>')
def Error(message):
	return render_template('error.html',message=message)
@app.errorhandler(404)
def Error_404(e):
	flash(r'## 404 not found \n指挥官大人,您访问的页面......没有找到......QAQ.','error')
	return sites.modules.Page_Back()
@app.route('/blank')
def Blank():
	return render_template('base.html')

@app.route('/')
def Home():
	return sites.home.Run()

@app.route('/problemlist')
def Problemlist():
	return sites.problemlist.Run()
@app.route('/problem/<int:problemid>',methods=['GET','POST'])
def Problem(problemid):
	return sites.problem.Run(int(problemid))
@app.route('/problemadd',methods=['GET','POST'])
def Problemadd():
	return sites.problemadd.Run()
@app.route('/problem/<int:problem_id>/edit',methods=['GET','POST'])
def Problemedit(problem_id):
	return sites.problemedit.Run(problem_id)
@app.route('/problem/<int:problem_id>/delete')
def Problemdel(problem_id):
	return sites.problemdel.Run(problem_id)

@app.route('/contestlist')
def Contestlist():
	return sites.contestlist.Run()
@app.route('/contestadd',methods=['GET','POST'])
def Contestadd():
	return sites.contestadd.Run()
@app.route('/contest/<int:id>')
def Contest(id):
	return sites.contest.Run(id)
@app.route('/contest/<int:contest_id>/problem/<int:problem_id>',methods=['GET','POST'])
def Contest_Problem(contest_id,problem_id):
	return sites.contest_problem.Run(contest_id,problem_id)
@app.route('/contest/<int:contest_id>/submissions/my')
def Contest_Submissions_My(contest_id):
	return sites.contest_submissions.Submissions_My(contest_id)
@app.route('/contest/<int:contest_id>/submissions')
def Contest_Submissions_All(contest_id):
	return sites.contest_submissions.Submissions_All(contest_id)
@app.route('/contest/<int:contest_id>/ranklist')
def Contest_Ranklist(contest_id):
	return sites.contest_ranklist.Run(contest_id)
@app.route('/contest/<int:contest_id>/statistic')
def Contest_Statistic(contest_id):
	return sites.contest_statistic.Run(contest_id)

@app.route('/help')
def Help():
	return render_template('help.html')

@app.route('/about')
def About():
	return render_template('about.html')
@app.route('/zhongwuchishenme')
def Zhongwuchishenme():
	return render_template('tools/zhongwuchishenme.html')

@app.route('/status')
def Status():
	return sites.status.Run()
@app.route('/record/<int:record_id>',methods=['GET','POST'])
def Record(record_id):
	return sites.record.Run(record_id)
@app.route('/record/<int:record_id>/ref')
def Record_Refresh(record_id):
	return sites.record.Refresh(record_id)

@app.route('/login',methods=['GET','POST'])
def Login():
	return sites.login.Run()
@app.route('/logout')
def Logout():
	try:
		resp = Response(render_template('jumpto.html',link='/'))
		resp.delete_cookie('username')
		resp.delete_cookie('client_key')
		return resp
	except:
		return redirect('/')

@app.route('/register',methods=['GET','POST'])
def Register():
	return sites.register.Run()

@app.route('/user/<username>')
def Userhome(username):
	return sites.userhome.Run(username)
@app.route('/user/<username>/edit',methods=['GET','POST'])
def Useredit(username):
	return sites.useredit.Run(username)

# app.secret_key = hashlib.sha256(str(random.randint(-1000000000,1000000000)).encode('utf-8')).hexdigest()
app.secret_key = '你知道也没事反正我不用这个'
