from flask import *
from .problem import *
import json

def Run(pid):
	uproblem = Getproblem(pid)
	if uproblem == None:
		return render_template('error.html',message="题目P%d没找着!\n可能是因为编号不对."%pid)
	uproblem = json.loads(uproblem[1])

	uproblem['pid'] = pid
	return render_template('problem.html',uproblem=uproblem)
