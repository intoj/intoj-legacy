#coding:utf-8
import pymysql

db_password = '24'

def Is_Connect():
	db = pymysql.connect("localhost","intlsy",db_password,"intoj")
	cur = db.cursor()
	return db,cur
def End_Connect(db,cur):
	cur.close()
	db.close()

def Read_Problem(id):
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM problems where id=%s",id)
	uproblem = cur.fetchone()
	End_Connect(db,cur)
	return uproblem
def Read_Problemlist(order='id'):
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM problems ORDER BY %s",order)
	problemlist = cur.fetchall()
	End_Connect(db,cur)
	return problemlist

def Read_Contest(id):
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM contests where id=%s",id)
	contest = cur.fetchone()
	End_Connect(db,cur)
	return contest
def Read_Contestlist():
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM contests ORDER BY id DESC")
	contestlist = cur.fetchall()
	End_Connect(db,cur)
	return contestlist

def Read_Record(id):
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM records WHERE id=%s;",id)
	urecord = cur.fetchone()
	End_Connect(db,cur)
	return urecord
def Read_Recordlist():
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM records ORDER BY id DESC")
	recordlist = cur.fetchall()
	End_Connect(db,cur)
	return recordlist

def Read_User_Byname(username):
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM users WHERE username=%s;",username)
	uuser = cur.fetchone()
	End_Connect(db,cur)
	return uuser

def Execute(cmd,arg=None):
	db,cur = Is_Connect()
	if arg == None: cur.execute(cmd)
	else: cur.execute(cmd,arg)
	db.commit()
	End_Connect(db,cur)

def Fetchone(cmd,arg=None):
	db,cur = Is_Connect()
	if arg == None: cur.execute(cmd)
	else: cur.execute(cmd,arg)
	ret = cur.fetchone()
	End_Connect(db,cur)
	return ret

def User_Privilege(username,privilege_id):
	user = Read_User_Byname(username)
	if user == None: return 0
	if user[7]: return 1
	return user[privilege_id+7]
