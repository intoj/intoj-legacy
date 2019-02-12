#coding:utf-8
from flask import *
from .statuslist import *
from ..modules import *

def Run():
	statuslist = list(Getstatuslist())
	for i in range(len(statuslist)):
		statuslist[i] = list(statuslist[i])
		uscore = statuslist[i][5]
		if int(uscore) == uscore: uscore = int(uscore)
		statuslist[i][5] = uscore
	return render_template('status.html',statuslist=statuslist)
