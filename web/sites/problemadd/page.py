from flask import *
import pymysql

def Run():
	return render_template("problemadd.html")

def Getid():
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT COUNT(*) FROM problems;")
	id = int(cur.fetchone()[0])+1
	db.close()
	return id
def Submit(req):
	id = Getid()
	index = "'%s','%s','%s','%s','%s','%s',%s,%s" % \
			(req['title'],req['description'],req['input_format'],req['output_format'],\
			req['example'],req['limit_and_hint'],req['time_limit'],req['memory_limit'])

	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cmd = "INSERT INTO problems VALUES(%d,%s);" % (id,index)
	cur.execute(cmd)

	db.commit()
	db.close()

	return id
