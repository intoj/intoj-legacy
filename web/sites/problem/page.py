#coding:utf-8
from flask import *
from .problem import *
from ..modules import *

def Run(id):
	uproblem = Getproblem(id)
	if uproblem == None:
		flash('题目 P%d 没找着!\n可能是因为编号不对.'%id,'error')
		return redirect('/problemlist')
	return render_template('problem.html',uproblem=uproblem)
