#coding:utf-8
from flask import *
import pymysql
import hashlib,re
from ..modules import *

def Register(req):
	username,password,ensure_password,email = req['username'],req['password'],req['ensure_password'],req['email']

	if username == '': return 0,'用户名不能为空'
	if password == '': return 0,'密码不能为空'
	if password != ensure_password: return 0,'两次输入的密码不同'
	if email == '': return 0,'邮箱地址不能为空'

	if not Vaild_Username(username):
		return 0,'用户名只能包含大小写字母,数字,下划线和减号'

	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()

	cur.execute("SELECT COUNT(*) FROM users WHERE username=%s;",username)
	count = int(cur.fetchone()[0])
	if count != 0: return 0,'用户名已被占用'

	password_sha256 = hashlib.sha256(password.encode('utf-8')).hexdigest()
	password_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest()
	cur.execute("INSERT INTO users(`username`,`password_sha256`,`password_sha1`,`email`,`nameplate`) VALUES(%s,%s,%s,%s,'');",(username,password_sha256,password_sha1,email))

	db.commit()
	db.close()

	return 1,''
