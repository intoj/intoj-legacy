from flask import *
import pymysql

def Getproblemlist():
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM problems ORDER BY pid")
	problemlist = cur.fetchall()
	db.close()
	return problemlist
