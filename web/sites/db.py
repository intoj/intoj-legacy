#coding:utf-8
import pymysql

db_password = '24'

def Is_Connect():
	global db,cur
	db = pymysql.connect("localhost","intlsy",db_password,"intoj")
	cur = db.cursor()

def Read_Problem(id):
	Is_Connect()
	cur.execute("SELECT * FROM problems where id=%s",id)
	uproblem = cur.fetchone()
	return uproblem
def Read_Problemlist(order='id'):
	Is_Connect()
	cur.execute("SELECT * FROM problems ORDER BY %s",order)
	problemlist = cur.fetchall()
	return problemlist

def Read_Record(id):
	Is_Connect()
	cur.execute("SELECT * FROM records WHERE id=%s;",id)
	urecord = cur.fetchone()
	return urecord
def Read_Recordlist():
	Is_Connect()
	cur.execute("SELECT * FROM records ORDER BY id DESC")
	recordlist = cur.fetchall()
	return recordlist

def Read_User_Byname(username):
	Is_Connect()
	cur.execute("SELECT * FROM users WHERE username=%s;",username)
	uuser = cur.fetchone()
	return uuser

def Execute(cmd,arg=None):
	Is_Connect()
	if arg == None: cur.execute(cmd)
	else: cur.execute(cmd,arg)
	db.commit()

def Fetchone(cmd,arg=None):
	Is_Connect()
	if arg == None: cur.execute(cmd)
	else: cur.execute(cmd,arg)
	return cur.fetchone()
