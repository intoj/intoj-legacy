#coding:utf-8
from flask import *
import pymysql
from ..modules import *

def Run(username):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM users WHERE username=%s;",username)
	userdata = cur.fetchone()
	db.close()

	if userdata == None:
		flash('用户 %s 不存在'%username,'error')
		return redirect('/')
	else:
		userdata = list(userdata)
		return render_template('useredit.html',user=userdata)

def Useredit(username,req):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()

	cur.execute("UPDATE users SET `nameplate`=%s,`email`=%s WHERE username=%s;",(req['nameplate'],req['email'],username))

	db.commit()
	db.close()
