from flask import *
import pymysql

def Getproblem(id):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM problems where id=%s" % str(id))
	uproblem = cur.fetchone()
	db.close()
	return uproblem
