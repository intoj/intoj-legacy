#coding:utf-8
from flask import *
import hashlib,re
import db,modules

def Can_Login(req):
	username,password = req['username'],req['password']

	if username == '': return 0,'用户名不能为空'
	if password == '': return 0,'密码不能为空'
	if not modules.Vaild_Username(username):
		return 0,'用户名只能包含大小写字母,数字,下划线和减号'

	nowuser = db.Read_User_Byname(username)
	if nowuser == None: return 0,'并没有这个用户'

	password_sha256 = hashlib.sha256(password.encode('utf-8')).hexdigest()
	password_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest()
	if password_sha256 != nowuser[2] or password_sha1 != nowuser[3]:
		return 0,'密码不对'

	client_key_raw = username + password_sha256 + password_sha1;
	client_key = hashlib.sha256(client_key_raw.encode('utf-8')).hexdigest()
	return 1,client_key

def Run():
	if request.method == 'GET':
		return render_template('login.html')
	else:
		is_success,message = Can_Login(request.form)
		if not is_success:
			flash(message,'error')
			return render_template('login.html')
		else:
			username = request.form['username']
			modules.Set_Session('client_keys',username,message)
			# 此时message就是clientkey
			link = request.args['url'] if 'url' in request.args else '/'
			resp = make_response(redirect(link))
			resp.set_cookie('username',username,max_age=60*60*24*30)
			resp.set_cookie('client_key',message,max_age=60*60*24*30)
			flash(r'登录成功','ok')
			return resp
