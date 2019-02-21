#coding:utf-8
from flask import *
import db,modules

def Run(username):
	userdata = db.Fetchone("SELECT * FROM users WHERE username=%s;",username)

	if userdata == None:
		flash('用户 %s 不存在'%username,'error')
		return redirect('/')
	else:
		userdata = list(userdata)
		return render_template('useredit.html',user=userdata)

def Useredit(username,req):
	db.Execute("UPDATE users SET `nameplate`=%s,`email`=%s WHERE username=%s;",(req['nameplate'],req['email'],username))
