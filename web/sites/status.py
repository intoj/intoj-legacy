#coding:utf-8
from flask import *
import db,modules

def Run():
	statuslist = list(db.Read_Recordlist())
	for i in range(len(statuslist)):
		statuslist[i] = list(statuslist[i])
		uscore = statuslist[i][5]
		if int(uscore) == uscore: uscore = int(uscore)
		statuslist[i][5] = uscore
	return render_template('status.html',statuslist=statuslist)
