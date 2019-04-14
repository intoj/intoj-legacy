#coding:utf-8
from flask import *
import db,modules

def Change(origin_id,req):
	id = req['id']
	if req['id'] == '': id = origin_id
	else:
		if int(req['id']) < 0:
			flash(r'编号不可以为负','error')
			return modules.Page_Back()
		count = int(db.Fetchone('SELECT COUNT(*) FROM problems WHERE id=%s',req['id'])['COUNT(*)'])
		if count > 0:
			flash(r'题目编号 %s 已经有过了.'%req['id'],'error')
			modules.Page_Back()

	is_public = 1 if req.get('is_public') == 'on' else 0
	db.Execute("UPDATE problems SET `id`=%s,`title`=%s,`description`=%s,`input_format`=%s,`output_format`=%s,\
			`example`=%s,`limit_and_hint`=%s,`time_limit`=%s,`memory_limit`=%s,`is_public`=%s\
			 WHERE id=%s;",(id,req['title'],req['description'],req['input_format'],req['output_format'],
 			req['example'],req['limit_and_hint'],req['time_limit'],req['memory_limit'],is_public,origin_id))

	return redirect('/problem/%s'%id)

def Run(origin_id):
	if not modules.Current_User_Privilege('is_problem_manager'):
		flash(r'无此权限','error')
		return modules.Page_Back()
	problem = db.Read_Problem(origin_id)
	if problem == None:
		flash(r'### 题目 P%d 没找着! \n 可能是因为编号不对.'%origin_id,'error')
		return modules.Page_Back()

	if request.method == 'GET':
		return render_template("problemedit.html",problem=problem)
	else:
		return Change(origin_id,request.form)
