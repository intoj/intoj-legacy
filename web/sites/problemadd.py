#coding:utf-8
from flask import *
import pymysql
import db,modules

def Run():
	return render_template("problemadd.html")

# 返回 is_success, id, message
def Submit(req):
	is_public = 1 if req.get('is_public') != None else 0
	id = req['id']
	if req['id'] != '':
		if int(req['id']) <= 0:
			return 0,0,'编号必须为正'
		count = int(db.Fetchone('SELECT COUNT(*) FROM problems WHERE id=%s',req['id'])[0])
		if count > 0:
			return 0,0,'题目编号 %s 已经有过了.'%req['id']
		db.Execute("INSERT INTO problems VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(req['id'],req['title'],req['description'],req['input_format'],req['output_format'],\
		req['example'],req['limit_and_hint'],req['time_limit'],req['memory_limit'],is_public))
	else:
		id = 1
		count = int(db.Fetchone('SELECT COUNT(*) FROM problems')[0])
		if count > 0:
			id = int(db.Fetchone('SELECT MAX(id) FROM problems')[0]) + 1
		db.Execute("INSERT INTO problems VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(id,req['title'],req['description'],req['input_format'],req['output_format'],\
		req['example'],req['limit_and_hint'],req['time_limit'],req['memory_limit'],is_public))

	return 1,id,''
