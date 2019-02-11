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
		return render_template('error.html',message="用户 %s 不存在"%username)
	else:
		userdata = list(userdata)
		userdata.append(Email_Hash(userdata[4]))
		return render_template('userhome.html',user=userdata)
