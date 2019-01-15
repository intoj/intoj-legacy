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

def Color(a,fullscore=100):
	if a < fullscore*0.3: return "red"
	if a < fullscore*0.6: return "orange"
	if a < fullscore: return "forestgreen"
	return "#00ee00"

def SubtaskColor(status):
	if status == "Accepted": return "#00ee00"
	return "red"

def Run(id):
	record = Getrecord(id)
	if record == None:
		return render_template('error.html',message="评测记录R%d没找着!\n可能是因为编号不对."%id)

	record = list(record)
	status = record[4]
	score = record[5]
	if int(score) == score: score = int(score)
	record[5] = score
	record.append(tostatus[status])
	record.append(statusicon[status])
	record.append(Color(score))

	result = json.loads(record[7])
	subtasks = []
	for i in result['subtasks']:
		status = i['status']
		i['status_name'] = tostatus[status]
		i['status_icon'] = statusicon[status]
		i['score_color'] = SubtaskColor(status)
		score = i['score']
		if int(score) == score: score = int(score)
		i['score'] = score
		subtasks.append(i)

	return render_template('record.html',record=record,subtasks=subtasks)
