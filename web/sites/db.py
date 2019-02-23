#coding:utf-8
import pymysql

db_password = '24'

def Is_Connect():
	global db,cur
	db = pymysql.connect("localhost","intlsy",db_password,"intoj")
	cur = db.cursor()
def End_Connect():
	global db,cur
	cur.close()
	db.close()

def Read_Problem(id):
	Is_Connect()
	cur.execute("SELECT * FROM problems where id=%s",id)
	uproblem = cur.fetchone()
	End_Connect()
	return uproblem
def Read_Problemlist(order='id'):
	Is_Connect()
	cur.execute("SELECT * FROM problems ORDER BY %s",order)
	problemlist = cur.fetchall()
	End_Connect()
	return problemlist

def Read_Record(id):
	Is_Connect()
	cur.execute("SELECT * FROM records WHERE id=%s;",id)
	urecord = cur.fetchone()
	End_Connect()
	return urecord
def Read_Recordlist():
	Is_Connect()
	cur.execute("SELECT * FROM records ORDER BY id DESC")
	recordlist = cur.fetchall()
	End_Connect()
	return recordlist

def Read_User_Byname(username):
	Is_Connect()
	cur.execute("SELECT * FROM users WHERE username=%s;",username)
	uuser = cur.fetchone()
	End_Connect()
	return uuser

def Execute(cmd,arg=None):
	Is_Connect()
	if arg == None: cur.execute(cmd)
	else: cur.execute(cmd,arg)
	db.commit()
	End_Connect()

def Fetchone(cmd,arg=None):
	Is_Connect()
	if arg == None: cur.execute(cmd)
	else: cur.execute(cmd,arg)
	End_Connect()
	return cur.fetchone()
