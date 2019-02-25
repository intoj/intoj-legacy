#coding:utf-8
from flask import *
import db,modules

def Run(id):
	problem = db.Read_Problem(id)
	if problem == None:
		flash(r'### 题目 P%d 没找着! \n 可能是因为编号不对.'%id,'error')
		return modules.Page_Back()
	if not problem[9]:
		if not modules.Is_Loggedin() or not db.User_Privilege(request.cookies['username'],2):
			flash('无此权限','error')
			return modules.Page_Back()
	return render_template('problem.html',uproblem=problem)
