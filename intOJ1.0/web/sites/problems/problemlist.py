from flask import *
import pymysql

db = pymysql.connect("localhost","intlsy","24","intoj")
cur = db.cursor()

def Getproblemlist():
	cur.execute("SELECT * FROM problems")
	problemlist = cur.fetchall()
	return problemlist
