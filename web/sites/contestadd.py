#coding:utf-8
from flask import *
import datetime
import db,modules

date_format = '%Y-%m-%d %H:%M:%S'

def Contestadd(req):
	id = 1
	count = int(db.Fetchone('SELECT COUNT(*) FROM contests')['COUNT(*)'])
	if count > 0:
		id = int(db.Fetchone('SELECT MAX(id) FROM contests')['MAX(id)']) + 1

	req_problems = req['problems'].split(',')
	problems = []
	for problem in req_problems:
		if db.Read_Problem(problem) == None:
			flash(r'题目#%s不存在'%problem,'error')
			return modules.Page_Back()
		problems.append({'id':int(problem)})

	try:
		begin_time = datetime.datetime.strptime(req['begin_time'],date_format)
		end_time = datetime.datetime.strptime(req['end_time'],date_format)
	except:
		flash(r'日期格式不对. 应为 yyyy-mm-dd HH:MM:SS','error')
		return modules.Page_Back()

	db.Execute('INSERT INTO contests VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
				id,req['title'],req['subtitle'],req['begin_time'],req['end_time'],
				req['description'],'{"type":"oi-intoj"}',request.cookies['username'],json.dumps(problems),''))
	flash('添加成功','ok')
	return redirect('/contest/%d'%id)

def Run():
	if not modules.Current_User_Privilege('is_contest_manager'):
		flash(r'无此权限','error')
		return modules.Page_Back()

	if request.method == 'GET':
		current_date = datetime.datetime.now().strftime(date_format)
		return render_template("contestadd.html",current_date=current_date)
	else:
		return Contestadd(request.form)
