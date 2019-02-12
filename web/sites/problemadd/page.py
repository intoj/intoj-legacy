#coding:utf-8
from flask import *
import pymysql
from ..modules import *

def Run():
	return render_template("problemadd.html")

# 返回 is_success, id, message
def Submit(req):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	id = req['id']
	if req['id'] != '':
		cur.execute('SELECT COUNT(*) FROM problems WHERE id=%s',req['id'])
		count = int(cur.fetchone()[0])
		if count > 0:
			return 0,0,'题目编号 %s 已经有过了.'%req['id']
		cur.execute("INSERT INTO problems VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);",(req['id'],req['title'],req['description'],req['input_format'],req['output_format'],\
		req['example'],req['limit_and_hint'],req['time_limit'],req['memory_limit']))
	else:
		id = 1
		cur.execute('SELECT COUNT(*) FROM problems')
		count = int(cur.fetchone()[0])
		if count > 0:
			cur.execute('SELECT MAX(id) FROM problems')
			id = int(cur.fetchone()[0])+1
		cur.execute("INSERT INTO problems VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s);",(id,req['title'],req['description'],req['input_format'],req['output_format'],\
		req['example'],req['limit_and_hint'],req['time_limit'],req['memory_limit']))

	db.commit()
	db.close()

	return 1,id,''
