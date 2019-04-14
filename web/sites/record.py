#coding:utf-8
from flask import *
import json,datetime
import db,modules,newsubmit,tool_total_ac_submit_recalculate

def Get(id):
	record = db.Read_Record(id)
	if record == None:
		flash(r'### 提交记录R%d没找着! \n 可能是因为编号不对.'%id,'error')
		return redirect('/status')

	if record['contest_id']:
		end_time = datetime.datetime.strptime(db.Read_Contest(record['contest_id'])['end_time'],'%Y-%m-%d %H:%M:%S')
		now_time = datetime.datetime.now()
		if now_time < end_time:
			if request.cookies['username'] != record['username'] and not modules.Current_User_Privilege('is_contest_manager'):
				flash(r'这是比赛时的提交, 您无权查看','error')
				return modules.Page_Back()
	elif not db.Read_Problem(record['problem_id'])['is_public'] and not modules.Current_User_Privilege('is_problem_manager') and record['username'] != modules.Current_User():
		flash(r'该题目尚未公开, 您无权查看','error')
		return modules.Page_Back()

	result = json.loads(record['result'])
	subtasks = result['subtasks']
	contest = db.Read_Contest(record['contest_id']) if record['contest_id'] else None
	return render_template('record.html',record=record,subtasks=subtasks,contest=contest)

def Run(record_id):
	if request.method == 'GET':
		return Get(record_id)
	else:
		if not modules.Current_User_Privilege('is_problem_manager'):
			flash(r'无此权限','error')
			return modules.Page_Back()
		return newsubmit.Rejudge(record_id)

def Refresh(id):
	record = db.Read_Record(id)
	if record == None:
		return '{ "success": 0, "message": "刷新状态失败: id%s不存在" }'%id

	ret = {
		'record': record,
		'success': 1
	}

	if record['status'] >= 2:
		tool_total_ac_submit_recalculate.Total_Ac_Submit_Recalculate(record['username'])

	return json.dumps(ret)
