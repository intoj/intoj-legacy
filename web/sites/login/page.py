#coding:utf-8
from flask import *
import pymysql
import hashlib,re
from ..modules import *

def Can_Login(req):
	username,password = req['username'],req['password']

	if username == '': return 0,'用户名不能为空'
	if password == '': return 0,'密码不能为空'
	if not Vaild_Username(username):
		return 0,'用户名只能包含大小写字母,数字,下划线和减号'

	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()

	cur.execute("SELECT * FROM users WHERE username=%s;",username)
	nowuser = cur.fetchone()
	if nowuser == None: return 0,'并没有这个用户'

	password_sha256 = hashlib.sha256(password.encode('utf-8')).hexdigest()
	password_sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest()
	if password_sha256 != nowuser[2] or password_sha1 != nowuser[3]:
		return 0,'密码不对'

	client_key_raw = username + password_sha256 + password_sha1;
	client_key = hashlib.sha256(client_key_raw.encode('utf-8')).hexdigest()
	return 1,client_key
