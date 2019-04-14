#coding:utf-8
from flask import *
import pymysql
import db,modules

def Run(problem_id):
	if not modules.Current_User_Privilege('is_problem_manager'):
		flash(r'无此权限','error')
		return modules.Page_Back()
	db.Execute("DELETE FROM problems WHERE id=%s",problem_id)
	return redirect('/problemlist')
