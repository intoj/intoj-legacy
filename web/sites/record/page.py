from flask import *
import pymysql

statuslist = {
"Accepted":"ok",
"Wrong Answer":"remove",
"Waiting":"spinner icon-spin",
"Running":"spinner icon-spin",
"Time Limit Exceed":"time",
"Memory Limit Exceed":"hdd",
"Runtime Error":"asterisk",
"Compile Error":"github-alt"
}
def Color(a):
	if a < 30: return "red"
	if a < 60: return "orange"
	if a < 100: return "forestgreen"
	return "#00ee00"
def SubtaskColor(a):
	if a == "Accepted": return "#00ee00"
	return "red"

def Run(rid):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM records WHERE rid=%d;" % rid)
	urecord = cur.fetchone()
	db.close()
	if urecord == None:
		return render_template('error.html',message="评测记录R%d没找着!\n可能是因为编号不对."%rid)
	subtaskstatus = []  # (status,score,time,memory)
	subtaskicon = []
	subtaskcolor = []
	subtasks = (urecord[7].split('\n'))[1:]
	testcasecnt = len(subtasks)
	for i in range(0,testcasecnt,2):
		ustatus = subtasks[i]
		ps = subtasks[i+1].split()
		uscore = int(ps[0])
		utime = int(ps[1])
		umemory = int(ps[2])
		subtaskstatus.append((ustatus,uscore,utime,umemory))
		subtaskicon.append(statuslist[ustatus])
		subtaskcolor.append(SubtaskColor(ustatus))
	return render_template('record.html',urecord=urecord,statusicon=statuslist[urecord[2]],scorecolor=Color(int(urecord[3])),
							subtaskstatus=subtaskstatus,subtaskicon=subtaskicon,subtaskcolor=subtaskcolor)
