#coding:utf-8
from flask import *
import pymysql
from ..modules import *

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

	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("INSERT INTO problems VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);",(id,Raw(req['title']),Raw(req['description']),Raw(req['input_format']),Raw(req['output_format']),\
	Raw(req['example']),Raw(req['limit_and_hint']),Raw(req['time_limit']),Raw(req['memory_limit'])))

	db.commit()
	db.close()

	return id
