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
	9:"Partical Accepted",
	10:"Accepted"
}

statusicon = {
	"Waiting":"spinner icon-spin",
	"Running":"spinner icon-spin",
	"Unknown Error":"thumbs-down",
	"Compile Error":"github-alt",
	"Hacked":"magic",
	"Wrong Answer":"remove",
	"Time Limit Exceed":"time",
	"Memory Limit Exceed":"hdd",
	"Runtime Error":"asterisk",
	"Partical Accepted":"legal",
	"Accepted":"ok"
}

def Color(a):
	if a < 30: return "red"
	if a < 60: return "orange"
	if a < 100: return "forestgreen"
	return "#00ee00"

def Run():
	stlist = Getstatuslist()
	statuslist = []
	for i in stlist:
		decoded = json.loads(i[1]);
		decoded['rid'] = int(i[0])
		decoded['statusname'] = tostatus[decoded['status']]
		decoded['icon'] = statusicon[decoded['statusname']]
		decoded['scorecolor'] = Color(decoded['score'])
		statuslist.append(decoded)
	return render_template('status.html',statuslist=statuslist)
