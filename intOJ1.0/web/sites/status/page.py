from flask import *
from .recordlist import *

statuslist = {
"Accepted":"ok",
"Wrong Answer":"remove",
"Waiting":"spinner icon-spin",
"Running":"spinner icon-spin",
"Time Limit Exceed":"time",
"Runtime Error":"asterisk"
}
def Color(a):
	if a < 30: return "red"
	if a < 60: return "orange"
	if a < 100: return "forestgreen"
	return "#00ee00"

def Run():
	recordlist = Getrecordlist()
	statusicon = []
	color = []
	for i in range(len(recordlist)):
		statusicon.append(statuslist[recordlist[i][2]])
		color.append(Color(recordlist[i][3]))
	return render_template('status.html',recordlist=recordlist,scorecolor=color,statusicon=statusicon)
