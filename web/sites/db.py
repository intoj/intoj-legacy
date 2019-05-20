#coding:utf-8
import pymysql
import modules,config

def Generate_Limitation(limitation,allowed=[]):
	if limitation == None: return '',[]
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

def Connect():
	db_name = config.config['database']['name']
	db_user = config.config['database']['user']
	db_host = config.config['database']['host']
	db_pass = config.config['database']['pass']
	db = pymysql.connect(db_host,db_user,db_pass,db_name)
	cur = db.cursor(cursor=pymysql.cursors.DictCursor)
	return db,cur
def End_Connect(db,cur):
	cur.close()
	db.close()

def Read_Problem(id):
	db,cur = Connect()
	cur.execute("SELECT * FROM problems where id=%s",id)
	uproblem = cur.fetchone()
	End_Connect(db,cur)
	return uproblem
def Read_Problemlist(order='id'):
	db,cur = Connect()
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
	db,cur = Connect()
	lim,arg = Generate_Limitation(limitation,allowed)
	cmd = "SELECT * FROM records %s ORDER BY %s" % (lim,modules.Raw(order))
	cur.execute(cmd,arg)
	submissions = cur.fetchall()
	End_Connect(db,cur)
	return submissions

def Read_Contest(id):
	db,cur = Connect()
	cur.execute("SELECT * FROM contests where id=%s",id)
	contest = cur.fetchone()
	End_Connect(db,cur)
	return contest
def Read_Contestlist():
	db,cur = Connect()
	cur.execute("SELECT * FROM contests ORDER BY id DESC")
	contestlist = cur.fetchall()
	End_Connect(db,cur)
	return contestlist
def Read_Contest_Ranklist(contest_id):
	db,cur = Connect()
	cur.execute("SELECT * FROM contest_players WHERE contest_id=%s",contest_id)
	ranklist = cur.fetchall()
	End_Connect(db,cur)
	if ranklist == None: return None
	return list(ranklist)

def Read_Record(id):
	db,cur = Connect()
	cur.execute("SELECT * FROM records WHERE id=%s;",id)
	record = cur.fetchone()
	End_Connect(db,cur)
	return record

def Read_Userlist():
	db,cur = Connect()
	cur.execute("SELECT * FROM users")
	userlist = cur.fetchall()
	End_Connect(db,cur)
	return userlist
def Read_User_Byname(username):
	db,cur = Connect()
	cur.execute("SELECT * FROM users WHERE username=%s;",username)
	user = cur.fetchone()
	End_Connect(db,cur)
	return user

def Execute(cmd,arg=None):
	db,cur = Connect()
	if arg == None: cur.execute(cmd)
	else: cur.execute(cmd,arg)
	db.commit()
	End_Connect(db,cur)

def Fetchone(cmd,arg=None):
	db,cur = Connect()
	if arg == None: cur.execute(cmd)
	else: cur.execute(cmd,arg)
	ret = cur.fetchone()
	End_Connect(db,cur)
	return ret

def Read_User_Privileges(username):
	db,cur = Connect()
	cur.execute("SELECT * FROM user_privileges WHERE username=%s;",username)
	user = cur.fetchone()
	End_Connect(db,cur)
	return user

def User_Privilege(username,privilege_name):
	if username == None: return 0
	user = Read_User_Privileges(username)
	if user == None: return 0
	if user['is_admin']: return 1
	return user[privilege_name]

def Read_Zisheng(limitation=None,top=10):
	allowed = {
		'id': ('eq','id'),
		'username': ('eq','username')
	}
	db,cur = Connect()

	lim,arg = Generate_Limitation(limitation,allowed)
	cmd = "SELECT * FROM zisheng %s ORDER BY id DESC LIMIT %d" % (lim,top)
	cur.execute(cmd,arg)
	zisheng = cur.fetchall()

	End_Connect(db,cur)
	return zisheng
