#coding:utf-8
from flask import *
import json
import db,modules

def Run(id):
	record = db.Read_Record(id)
	if record == None:
		flash(r'### 提交记录R%d没找着! \n 可能是因为编号不对.'%id,'error')
		return redirect('/status')

	record = list(record)
	status = record[4]
	score = record[5]
	if int(score) == score: score = int(score)
	record[5] = score

	result = json.loads(record[7])
	subtasks = []
	for i in result['subtasks']:
		score = i['score']
		if int(score) == score: score = int(score)
		i['score'] = score
		subtasks.append(i)

	return render_template('record.html',record=record,subtasks=subtasks)

def Refresh(id):
	record = db.Read_Record(id)
	if record == None:
		return '{ "success": 0, "message": "刷新状态失败: id%s不存在" }'%id

	record = list(record)
	status = record[4]
	score = record[5]
	if int(score) == score: score = int(score)
	record[5] = score

	result = json.loads(record[7])
	subtasks = []
	for i in result['subtasks']:
		score = i['score']
		if int(score) == score: score = int(score)
		i['score'] = score
		subtasks.append(i)

	record_html = render_template("record_overview.html",record=record)
	subtasks_html = render_template("record_subtasks.html",subtasks=subtasks)

	ret = {
		'record': record,
		'record_html': record_html,
		'score_color': modules.Score_Color(record[5]),
		'subtasks_html': subtasks_html,
		'success': 1
	}

	return json.dumps(ret)
