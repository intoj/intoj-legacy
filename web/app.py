#coding:utf-8
from flask import *
import sys,time,random
import hashlib,re
import sites
app = Flask(__name__)


@app.errorhandler(404)
def Error_404(e):
	return render_template('error.html',message="# $404\ not\ found$\n\n指挥官大人,您访问的页面......没有找到......QAQ.")

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
		runid,message = sites.newsubmit.page.Submit(int(problemid),request.form)
		if runid == -1: return render_template('error.html',message=message)
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

@app.route('/error/<message>')
def Error(message):
	return render_template('error.html',message=message)

@app.route('/status')
def Status():
	return sites.status.page.Run()

@app.route('/help')
def Help():
	return render_template('help.html')

@app.route('/about')
def About():
	return render_template('about.html')

@app.route('/record/<int:runid>',methods=['GET','POST'])
def Record(runid):
	if request.method == 'GET':
		return sites.record.page.Run(runid)
	else:
		is_success = sites.newsubmit.page.Rejudge(runid)
		if not is_success: return render_template('error.html',message="提交记录R%d没找着!\n可能是因为编号不对."%runid)
		else: return redirect('/record/%d'%runid)

@app.route('/login',methods=['GET','POST'])
def Login():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		is_success,message = sites.login.page.Can_Login(request.form)
		if not is_success: return render_template('login.html',message=message)
		else:
			username = request.form['username']
			session[username] = message
			# 此时message就是clientkey
			resp = Response(render_template('jumpto.html',link='/'))
			resp.set_cookie('username',username,max_age=60*60*24*30)
			resp.set_cookie('client_key',message,max_age=60*60*24*30)
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
		is_success,message = sites.register.page.Register(request.form)
		if not is_success: return render_template('register.html',message=message)
		else: return redirect('/login')

@app.route('/user/<username>')
def Userhome(username):
	return sites.userhome.page.Run(username)
@app.route('/user/<username>/edit',methods=['GET','POST'])
def Useredit(username):
	if request.method == 'GET':
		return sites.useredit.page.Run(username)
	else:
		pass

# app.secret_key = hashlib.sha256(str(random.randint(-1000000000,1000000000)).encode('utf-8')).hexdigest()
app.secret_key = '你知道也没事反正我不用这个'
