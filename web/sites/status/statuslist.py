from flask import *
import pymysql

def Getstatuslist():
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM records ORDER BY rid DESC")
	statuslist = cur.fetchall()
	db.close()
	return list(statuslist)