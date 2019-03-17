#coding:utf-8
import pymysql

db_password = '24'

def Generate_Limitation(limitation,allowed=[]):
	answer = ''
	arg = []
	for key,value in limitation.items():
		if value == None or key not in allowed or str(value).strip() == '': continue
		if answer != '': answer += " AND "
		operator = '=' if allowed[key][0] == 'eq' else '>=' if allowed[key][0] == 'ge' else '<='
		answer += '%s%s%%s' % (allowed[key][1],operator)
		arg.append(value)
	if answer != '':
		answer = 'WHERE ' + answer
	return answer,arg

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
def Read_Submissions(limitation=None,order="id DESC"):
	allowed = {
		'id': ('eq','id'),
		'problem_id': ('eq','problem_id'),
		'language': ('eq','language'),
		'status': ('eq','status'),
		'min_score': ('ge','score'),
		'max_score': ('le','score'),
		'username': ('eq','username'),
		'contest_id': ('eq','contest_id')
	}
	db,cur = Is_Connect()
	if limitation != None:
		lim,arg = Generate_Limitation(limitation,allowed)
		cmd = "SELECT * FROM records %s ORDER BY %s" % (lim,order)
		cur.execute(cmd,arg)
	else:
		cur.execute("SELECT * FROM records ORDER BY %s"%order)

	submissions = cur.fetchall()
	End_Connect(db,cur)
	return submissions

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
def Read_Contest_Ranklist(contest_id):
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM contest_players WHERE contest_id=%s",contest_id)
	ranklist = cur.fetchall()
	End_Connect(db,cur)
	if ranklist == None: return None
	return list(ranklist)

def Read_Record(id):
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM records WHERE id=%s;",id)
	urecord = cur.fetchone()
	End_Connect(db,cur)
	return urecord

def Read_Userlist():
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM users")
	userlist = cur.fetchall()
	End_Connect(db,cur)
	return userlist
def Read_User_Byname(username):
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM users WHERE username=%s;",username)
	user = cur.fetchone()
	End_Connect(db,cur)
	return user

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

def Read_User_Privileges(username):
	db,cur = Is_Connect()
	cur.execute("SELECT * FROM user_privileges WHERE username=%s;",username)
	user = cur.fetchone()
	End_Connect(db,cur)
	return user

def User_Privilege(username,privilege_id):
	if username == None: return 0
	user = Read_User_Privileges(username)
	if user == None: return 0
	if user[2]: return 1
	return user[privilege_id+2]
