from flask import *
import json,datetime
import db,modules,newsubmit

def Is_Exist(contest_id,problem_id):
	contest = db.Read_Contest(contest_id)
	if contest == None:
		flash('不存在的比赛','error')
		return 0,modules.Page_Back()
	begin_time = datetime.datetime.strptime(contest[3],'%Y-%m-%d %H:%M:%S')
	if begin_time > datetime.datetime.now():
		flash('比赛还未开始','error')
		return 0,modules.Page_Back()
	problem = db.Read_Problem(problem_id)
	if problem == None:
		flash('题目 P%d 没找着!'%problem_id,'error')
		return 0,modules.Page_Back()
	return 1,(problem,contest)

def Run(contest_id,problem_id):
	is_exist,ret = Is_Exist(contest_id,problem_id)
	if not is_exist: return ret
	return render_template('contest_problem.html',problem=ret[0],contest=ret[1])

def Submit(contest_id,problem_id,req):
	is_exist,ret = Is_Exist(contest_id,problem_id)
	if not is_exist: return ret
	return newsubmit.Submit(problem_id,req,contest_id)
