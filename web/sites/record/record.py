from flask import *
import pymysql

def Getrecord(runid):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM records WHERE rid=%d;" % runid)
	urecord = cur.fetchone()
	db.close()
	return urecord
