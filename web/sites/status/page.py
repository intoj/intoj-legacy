from flask import *
from .statuslist import *
from ..modules import *

def Run():
	statuslist = list(Getstatuslist())
	for i in range(len(statuslist)):
		statuslist[i] = list(statuslist[i])
		ustatus = statuslist[i][4]
		uscore = statuslist[i][5]
		if int(uscore) == uscore: uscore = int(uscore)
		statuslist[i][5] = uscore
		statuslist[i].append(tostatus[ustatus])
		statuslist[i].append(statusicon[ustatus])
		statuslist[i].append(Color(uscore))
	return render_template('status.html',statuslist=statuslist)
