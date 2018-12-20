from flask import *
from .record import *
import json

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

def Fromascii(s):
	a = ""
	s = s.split()
	for i in s:
		a += chr(int(i,16))
	return a

def Color(a,fullscore=100):
	if a < fullscore*0.3: return "red"
	if a < fullscore*0.6: return "orange"
	if a < fullscore: return "forestgreen"
	return "#00ee00"

def SubtaskColor(a):
	if a == "Accepted": return "#00ee00"
	return "red"

def Run(runid):
	urec = Getrecord(runid)
	if urec == None:
		return render_template('error.html',message="评测记录R%d没找着!\n可能是因为编号不对."%runid)

	urec = json.loads(urec[1])
	urec['rid'] = runid
	urec['code'] = Fromascii(urec['code'])
	urec['compilemessage'] = Fromascii(urec['compilemessage'])
	urec['statusname'] = tostatus[urec['status']]
	urec['icon'] = statusicon[urec['statusname']]
	urec['scorecolor'] = Color(urec['score'])
	for i in range(1,len(urec['subtask'])+1):
		u = urec['subtask'][str(i)]
		urec['subtask'][str(i)]['statusname'] = tostatus[u['status']]
		urec['subtask'][str(i)]['icon'] = statusicon[tostatus[u['status']]]
		urec['subtask'][str(i)]['scorecolor'] = Color(u['score'],u['fullscore'])
		urec['subtask'][str(i)]['judgermessage'] = Fromascii(u['judgermessage'])
		urec['subtask'][str(i)]['checkermessage'] = Fromascii(u['checkermessage'])

	return render_template('record.html',urec=urec)
