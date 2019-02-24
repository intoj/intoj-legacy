#coding: utf-8
import pymysql,json

db_password = '24'

def Is_Connect():
	global db,cur
	db = pymysql.connect("localhost","intlsy",db_password,"intoj")
	cur = db.cursor()
def End_Connect():
	global db,cur
	cur.close()
	db.close()

def Readproblem(id):
	Is_Connect()
	cur.execute("SELECT * FROM problems WHERE id=%d" % id)
	dbresult = cur.fetchone()
	print("\033[42;37mPROindex:\033[0m",dbresult)
	End_Connect()
	if dbresult == None: raise ValueError("无此题目")
	return dbresult[7],dbresult[8]

def Readrecord(id):
	Is_Connect()
	cur.execute("SELECT * FROM records WHERE id=%d"%id)
	dbresult = cur.fetchone()
	print("\033[42;37mRUNindex:\033[0m",dbresult)
	End_Connect()
	if dbresult == None: raise ValueError("无此记录")
	return dbresult[1],dbresult[2],dbresult

def Startjudge(rid):
	Is_Connect()
	cur.execute("UPDATE records SET status=1 WHERE id=%d" % rid)
	db.commit()
	End_Connect()

def Report(runid,status=2,score=0,time_usage=0,memory_usage=0,subtasks={'subtasks':[]},comp_message='',system_message=''):
	Is_Connect()
	cur.execute("UPDATE records SET status=%s,score=%s,time_usage=%s,memory_usage=%s,result=%s,compilation=%s,system_message=%s WHERE id=%s",
				(status,score,time_usage,memory_usage,json.dumps(subtasks),comp_message,system_message,runid))
	db.commit()
	End_Connect()

def CompileError(runid,message):
	Is_Connect()
	cur.execute("UPDATE records SET status=3 WHERE id=%s",runid)
	cur.execute("UPDATE records SET compilation=%s WHERE id=%s",(message,runid))
	db.commit()
	End_Connect()
