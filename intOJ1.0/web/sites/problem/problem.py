from flask import *
import pymysql

def Getproblem(pid):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM problems where pid=%s" % str(pid))
	uproblem = cur.fetchone()
	db.close()
	return uproblem
