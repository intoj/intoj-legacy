#coding:utf-8
from flask import *
import pymysql
import db,modules

# 返回 is_success, id, message
def Submit(req):
	is_public = 1 if req.get('is_public') != None else 0
	id = req['id']
	if req['id'] != '':
		if int(req['id']) <= 0:
			flash(r'编号必须为正','error')
			return render_template("problemadd.html")
		count = int(db.Fetchone('SELECT COUNT(*) FROM problems WHERE id=%s',req['id'])[0])
		if count > 0:
			flash(r'题目编号 %s 已经有过了.','error')
			return render_template("problemadd.html")
		db.Execute("INSERT INTO problems VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(req['id'],req['title'],req['description'],req['input_format'],req['output_format'],\
		req['example'],req['limit_and_hint'],req['time_limit'],req['memory_limit'],is_public))
	else:
		id = 1
		count = int(db.Fetchone('SELECT COUNT(*) FROM problems')[0])
		if count > 0:
			id = int(db.Fetchone('SELECT MAX(id) FROM problems')[0]) + 1
		db.Execute("INSERT INTO problems VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(id,req['title'],req['description'],req['input_format'],req['output_format'],\
		req['example'],req['limit_and_hint'],req['time_limit'],req['memory_limit'],is_public))

	return redirect('/problem/%s'%id)

def Run():
	if not modules.Current_User_Privilege(2):
		flash(r'无此权限','error')
		return modules.Page_Back()

	if request.method == 'GET':
		return render_template("problemadd.html")
	else:
		return Submit(request.form)
