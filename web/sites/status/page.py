from flask import *
from .statuslist import *

tostatus = {
	0:"Waiting",
	1:"Running",
	2:"Unknown Error",
	3:"Compile Error",
	4:"Hacked",
	5:"Wrong Answer",
	6:"Time Limit Exceed",
	7:"Memory Limit Exceed",
	8:"Runtime Error",
	9:"Partially Accepted",
	10:"Accepted"
}

statusicon = {
	0:"spinner icon-spin",
	1:"spinner icon-spin",
	2:"thumbs-down",
	3:"github-alt",
	4:"magic",
	5:"remove",
	6:"time",
	7:"hdd",
	8:"asterisk",
	9:"legal",
	10:"ok"
}

def Color(a):
	if a < 30: return "red"
	if a < 60: return "orange"
	if a < 100: return "forestgreen"
	return "#00ee00"

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
