from flask import *
from .problem import *
from ..modules import *

def Run(id):
	uproblem = Getproblem(id)
	if uproblem == None:
		return render_template('error.html',message="题目P%d没找着!\n可能是因为编号不对."%id)
	return render_template('problem.html',uproblem=uproblem)
