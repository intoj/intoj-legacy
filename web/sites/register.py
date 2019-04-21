#coding:utf-8
from flask import *
import hashlib,re
import db,modules

def Register(req):
	username,password,ensure_password,email = req['username'],req['password'],req['ensure_password'],req['email']

	if username == '': return 0,'用户名不能为空'
	if password == '': return 0,'密码不能为空'
	if password != ensure_password: return 0,'两次输入的密码不同'
	if email == '': return 0,'邮箱地址不能为空'

	if not modules.Vaild_Username(username):
		return 0,'用户名只能包含大小写字母,数字,下划线和减号'

	count = int(db.Fetchone("SELECT COUNT(*) FROM users WHERE username=%s;",username)['COUNT(*)'])
	if count != 0: return 0,'用户名已被占用'

	password_sha256 = hashlib.sha256(password.encode('utf-8')).hexdigest()
	password_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest()
	db.Execute("INSERT INTO users(`username`,`password_sha256`,`password_sha1`,`email`,`signature`,`total_ac`,`total_submit`) VALUES(%s,%s,%s,%s,'',0,0);",(username,password_sha256,password_sha1,email))

	return 1,''

def Run():
	if request.method == 'GET':
		return render_template('register.html')
	else:
		is_success,message = Register(request.form)
		if not is_success:
			flash(message,'error')
			return render_template('register.html')
		else:
			flash('注册成功','ok')
			return redirect('/login')
