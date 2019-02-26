#coding:utf-8
from flask import *
import db,modules

def Run(id):
	problem = db.Read_Problem(id)
	if problem == None:
		flash(r'### 题目 P%d 没找着! \n 可能是因为编号不对.'%id,'error')
		return modules.Page_Back()
	return render_template("problemedit.html",problem=problem)

def Change(origin_id,req):
	id = req['id']
	if req['id'] == '': id = origin_id
	else:
		if int(req['id']) < 0:
			return 0,0,'编号不可以为负'
		count = int(db.Fetchone('SELECT COUNT(*) FROM problems WHERE id=%s',req['id'])[0])
		if count > 0:
			return 0,0,'题目编号 %s 已经有过了.'%req['id']

	is_public = 1 if req.get('is_public') == 'on' else 0
	db.Execute("UPDATE problems SET `id`=%s,`title`=%s,`description`=%s,`input_format`=%s,`output_format`=%s,\
			`example`=%s,`limit_and_hint`=%s,`time_limit`=%s,`memory_limit`=%s,`is_public`=%s\
			 WHERE id=%s;",(id,req['title'],req['description'],req['input_format'],req['output_format'],
 			req['example'],req['limit_and_hint'],req['time_limit'],req['memory_limit'],is_public,origin_id))

	return 1,int(id),''
