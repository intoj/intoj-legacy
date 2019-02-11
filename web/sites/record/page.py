#coding:utf-8
from flask import *
from .record import *
import json
from ..modules import *

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
		score = i['score']
		if int(score) == score: score = int(score)
		i['score'] = score
		i['status_name'] = tostatus[status]
		i['status_icon'] = statusicon[status]
		i['score_color'] = Color(score,i['full_score'])
		subtasks.append(i)

	return render_template('record.html',record=record,subtasks=subtasks)
