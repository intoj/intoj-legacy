#coding:utf-8
from flask import *
from .record import *
import json
from ..modules import *

def Run(id):
	record = Getrecord(id)
	if record == None:
		flash('提交记录R%d没找着!\n可能是因为编号不对.'%id,'error')
		return redirect('/status')

	record = list(record)
	status = record[4]
	score = record[5]
	if int(score) == score: score = int(score)
	record[5] = score

	result = json.loads(record[7])
	subtasks = []
	for i in result['subtasks']:
		status = i['status']
		score = i['score']
		if int(score) == score: score = int(score)
		i['score'] = score
		subtasks.append(i)

	return render_template('record.html',record=record,subtasks=subtasks)
