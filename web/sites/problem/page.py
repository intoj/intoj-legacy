from flask import *
from .problem import *

def Run(pid):
	uproblem = Getproblem(pid)
	return render_template('problem.html',uproblem=uproblem)
