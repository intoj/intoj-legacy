from flask import *
from .problem import *
import json

def Fromascii(s):
	a = ""
	s = s.split()
	for i in s:
		a += chr(int(i,16))
	return a
def Run(pid):
	uproblem = Getproblem(pid)
	if uproblem == None:
		return render_template('error.html',message="题目P%d没找着!\n可能是因为编号不对."%pid)
	uproblem = json.loads(uproblem[1])
	uproblem['pid'] = pid
	uproblem['title'] = Fromascii(uproblem['title'])
	uproblem['description'] = Fromascii(uproblem['description'])
	uproblem['input'] = Fromascii(uproblem['input'])
	uproblem['output'] = Fromascii(uproblem['output'])
	uproblem['sample'] = Fromascii(uproblem['sample'])
	uproblem['hint'] = Fromascii(uproblem['hint'])
	return render_template('problem.html',uproblem=uproblem)
