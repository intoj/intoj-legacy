#coding:utf-8
from flask import *
import db,modules,newsubmit,config

def Run(problem_id):
	problem = db.Read_Problem(problem_id)
	if problem == None:
		flash(r'### 题目 P%d 没找着! \n 可能是因为编号不对.'%problem_id,'error')
		return modules.Page_Back()
	if not problem[9] and not modules.Current_User_Privilege(2):
		flash(r'无此权限','error')
		return modules.Page_Back()

	if request.method == 'GET':
		enable_lang = config.config['enable_lang']
		return render_template('problem.html',problem=problem,enable_lang=enable_lang)
	else:
		return newsubmit.Submit(problem_id,request.form)
