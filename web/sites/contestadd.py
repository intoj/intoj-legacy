from flask import *
import datetime
import db,modules

date_format = '%Y-%m-%d %H:%M:%S'

def Run():
	current_date = datetime.datetime.now().strftime(date_format)
	return render_template("contestadd.html",current_date=current_date)

def Contestadd(req):
	id = 1
	count = int(db.Fetchone('SELECT COUNT(*) FROM contests')[0])
	if count > 0:
		id = int(db.Fetchone('SELECT MAX(id) FROM contests')[0]) + 1

	req_problems = req['problems'].split(',')
	problems = []
	for problem in req_problems:
		if db.Read_Problem(problem) == None:
			return 0,0,'题目#%s不存在'%problem
		problems.append({'id':int(problem)})

	try:
		begin_time = datetime.datetime.strptime(req['begin_time'],date_format)
		end_time = datetime.datetime.strptime(req['end_time'],date_format)
	except:
		return 0,0,'日期格式不对. 应为 yyyy-mm-dd HH:MM:SS'

	db.Execute('INSERT INTO contests VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
				id,req['title'],req['subtitle'],req['begin_time'],req['end_time'],
				req['description'],'{"type":"oi-intoj"}',request.cookies['username'],json.dumps(problems),''))
	return 1,id,''
