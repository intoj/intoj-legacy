from flask import *
import pymysql

def Getrecordlist():
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM records ORDER BY rid")
	recordlist = cur.fetchall()
	db.close()
	return recordlist
