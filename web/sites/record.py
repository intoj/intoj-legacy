#coding:utf-8
from flask import *
import json,datetime
import db,modules

def Run(id):
	record = db.Read_Record(id)
	if record == None:
		flash(r'### 提交记录R%d没找着! \n 可能是因为编号不对.'%id,'error')
		return redirect('/status')

	if record[12]:
		end_time = datetime.datetime.strptime(db.Read_Contest(record[12])[4],'%Y-%m-%d %H:%M:%S')
		now_time = datetime.datetime.now()
		if now_time < end_time:
			if not modules.Is_Loggedin() or ( request.cookies['username'] != record[11] and not db.User_Privilege(request.cookies['username'],3) ):
				flash('这是比赛时的提交, 您无权查看','error')
				return modules.Page_Back()

	result = json.loads(record[7])
	subtasks = result['subtasks']
	contest = db.Read_Contest(record[12]) if record[12] else None
	return render_template('record.html',record=record,subtasks=subtasks,contest=contest)

def Refresh(id):
	record = db.Read_Record(id)
	if record == None:
		return '{ "success": 0, "message": "刷新状态失败: id%s不存在" }'%id

	result = json.loads(record[7])
	subtasks = result['subtasks']

	record_html = render_template("record_overview.html",record=record)
	subtasks_html = render_template("record_subtasks.html",subtasks=subtasks,record=record)

	ret = {
		'record': record,
		'record_html': record_html,
		'score_color': modules.Score_Color(record[5]),
		'subtasks_html': subtasks_html,
		'success': 1
	}

	return json.dumps(ret)
