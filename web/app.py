#coding:utf-8
from flask import *
import sys,os,time,random
import hashlib,re
workpath = os.path.dirname(os.path.abspath(sys.argv[1]))
print(workpath)
sys.path.insert(0,os.path.join(workpath,'sites'))
import sites

app = Flask(__name__)

app.add_template_global(sites.modules.Score_Color,'Score_Color')
app.add_template_global(sites.modules.tostatus,'tostatus')
app.add_template_global(sites.modules.statusicon,'statusicon')
app.add_template_global(sites.modules.Email_Hash,'Email_Hash')

@app.errorhandler(404)
def Error_404(e):
	flash(r'## 404 not found \n指挥官大人,您访问的页面......没有找到......QAQ.','error')
	return redirect('/')

@app.route('/')
def Home():
	return sites.home.Run()

@app.route('/problemlist')
def Problemlist():
	return sites.problemlist.Run()
@app.route('/problem/<int:problemid>',methods=['GET','POST'])
def Problem(problemid):
	if request.method == 'GET':
		return sites.problem.Run(int(problemid))
	else:
		runid,message = sites.newsubmit.Submit(int(problemid),request.form)
		if runid == -1:
			flash(message,'error')
			return sites.problem.Run(int(problemid))
		else: return redirect('/record/%d'%runid)
@app.route('/problemadd',methods=['GET','POST'])
def Problemadd():
	if request.method == 'GET':
		return sites.problemadd.Run()
	else:
		is_success,id,message = sites.problemadd.Submit(request.form)
		if not is_success:
			flash(message,'error')
			return sites.problemadd.Run()
		return redirect('/problem/%s' % id)
@app.route('/problem/<int:problemid>/edit',methods=['GET','POST'])
def Problemedit(problemid):
	if request.method == 'GET':
		return sites.problemedit.Run(problemid)
	else:
		is_success,newid,message = sites.problemedit.Change(problemid,request.form)
		if not is_success:
			flash(message,'error')
			return sites.problemedit.Run(problemid)
		return redirect('/problem/%s' % newid)
@app.route('/problem/<int:problemid>/delete',methods=['GET'])
def Problemdel(problemid):
	return sites.problemdel.Deleteproblem(problemid)

@app.route('/error/<message>')
def Error(message):
	return render_template('error.html',message=message)

@app.route('/status')
def Status():
	return sites.status.Run()

@app.route('/help')
def Help():
	return render_template('help.html')

@app.route('/about')
def About():
	return render_template('about.html')

@app.route('/record/<int:runid>',methods=['GET','POST'])
def Record(runid):
	if request.method == 'GET':
		return sites.record.Run(runid)
	else:
		is_success = sites.newsubmit.Rejudge(runid)
		if not is_success:
			flash(r'提交记录R%d没找着!\\\n可能是因为编号不对.'%runid,'error')
			return redirect('/status')
		else:
			flash('成功重测.','ok')
			return redirect('/record/%d'%runid)

@app.route('/login',methods=['GET','POST'])
def Login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		is_success,message = sites.login.Can_Login(request.form)
		if not is_success:
			flash(message,'error')
			return render_template('login.html')
		else:
			username = request.form['username']
			session[username] = message
			# 此时message就是clientkey
			resp = Response(render_template('jumpto.html',link='/'))
			resp.set_cookie('username',username,max_age=60*60*24*30)
			resp.set_cookie('client_key',message,max_age=60*60*24*30)
			flash('登录成功','ok')
			return resp
def Is_Loggedin():
	try:
		username = request.cookies['username']
		client_key = request.cookies['client_key']
		if session.get(username) != client_key: return 0
		else: return 1
	except: return 0
app.add_template_global(Is_Loggedin,'Is_Loggedin')

@app.route('/logout')
def Logout():
	try:
		resp = Response(render_template('jumpto.html',link='/'))
		resp.delete_cookie('username')
		resp.delete_cookie('client_key')
		return resp
	except:
		return render_template('jumpto.html',link='/')

@app.route('/register',methods=['GET','POST'])
def Register():
	if request.method == 'GET':
		print(request.cookies)
		return render_template('register.html')
	else:
		is_success,message = sites.register.Register(request.form)
		if not is_success:
			flash(message,'error')
			return render_template('register.html')
		else:
			flash('注册成功','ok')
			return redirect('/login')

@app.route('/user/<username>')
def Userhome(username):
	return sites.userhome.Run(username)
@app.route('/user/<username>/edit',methods=['GET','POST'])
def Useredit(username):
	if request.method == 'GET':
		return sites.useredit.Run(username)
	else:
		sites.useredit.Useredit(username,request.form)
		flash('修改成功','ok')
		return redirect('/user/%s'%username)

# app.secret_key = hashlib.sha256(str(random.randint(-1000000000,1000000000)).encode('utf-8')).hexdigest()
app.secret_key = '你知道也没事反正我不用这个'
