#coding: utf-8
import pymysql,json

db_password = '24'

def Is_Connect():
	global db,cur
	db = pymysql.connect("localhost","intlsy",db_password,"intoj")
	cur = db.cursor(cursor=pymysql.cursors.DictCursor)
def End_Connect():
	global db,cur
	cur.close()
	db.close()

def Read_Problem(id):
	Is_Connect()
	cur.execute("SELECT * FROM problems WHERE id=%d" % id)
	problem = cur.fetchone()
	print("\033[42;37mPROindex:\033[0m",problem)
	End_Connect()
	if problem == None: raise ValueError("无此题目")
	return problem

def Read_Record(id):
	Is_Connect()
	cur.execute("SELECT * FROM records WHERE id=%d"%id)
	record = cur.fetchone()
	print("\033[42;37mRUNindex:\033[0m",record)
	End_Connect()
	if record == None: raise ValueError("无此记录")
	return record

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

def Read_Contest_Player(username,contest_id):
	Is_Connect()
	cur.execute("SELECT * FROM contest_players WHERE username=%s AND contest_id=%s",(username,contest_id))
	info = cur.fetchone()
	End_Connect()
	if info == None: return {}
	else: return json.loads(info[3])

def Save_Contest_Player(username,contest_id,info):
	info = json.dumps(info)
	Is_Connect()
	cur.execute("SELECT COUNT(*) FROM contest_players WHERE username=%s AND contest_id=%s",(username,contest_id))
	if cur.fetchone()[0] == 0:
		cur.execute("INSERT INTO contest_players VALUES(NULL,%s,%s,%s)",(username,contest_id,info))
	else:
		cur.execute("UPDATE contest_players SET detail=%s WHERE username=%s AND contest_id=%s",(info,username,contest_id))
	db.commit()
	End_Connect()
