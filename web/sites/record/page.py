from flask import *
import pymysql

def Run(rid):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM records WHERE rid=%d;" % rid)
	urecord = cur.fetchone()
	db.close()
	if urecord == None:
		return render_template('error.html',message="评测记录R%d没找着!\n可能是因为编号不对."%rid)
	return render_template('record.html',urecord=urecord)
