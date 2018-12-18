from flask import *
import pymysql
import json
def Toascii(code):
	a = ""
	for i in code:
		a += hex(ord(i)) + ' '
	return a

def Run():
	return render_template("problemadd.html")

def Getpid():
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT COUNT(*) FROM problems;")
	pid = int(cur.fetchone()[0])+1
	db.close()
	return pid
def Submit(req):
	nreq = {
		'title':Toascii(req['title']),
		'description':Toascii(req['description']),
		'input':Toascii(req['input']),
		'output':Toascii(req['output']),
		'sample':Toascii(req['sample']),
		'hint':Toascii(req['hint']),
		'timelimit':int(req['timelimit']),
		'memorylimit':int(req['memorylimit'])
	}
	#print(nreq)
	index = json.dumps(nreq)
	#print(pjson)
	pid = Getpid()

	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cmd = "INSERT INTO problems VALUES(%d,'%s');" % (pid,index)
	cur.execute(cmd)

	db.commit()
	db.close()

	return pid
