#coding:utf-8
from flask import *
import db,modules

def Run(id):
	uproblem = db.Read_Problem(id)
	if uproblem == None:
		flash(r'### 题目 P%d 没找着! \n 可能是因为编号不对.'%id,'error')
		return redirect('/problemlist')
	return render_template('problem.html',uproblem=uproblem)
