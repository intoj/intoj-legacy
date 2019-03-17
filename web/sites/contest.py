from flask import *
import json
import db,modules

def Run(id):
	contest = db.Read_Contest(id)
	if contest == None:
		flash('不存在的比赛','error')
		return modules.Page_Back()
	problem_list = json.loads(contest[8])
	problems = [ db.Read_Problem(problem['id']) for problem in problem_list ]
	rule_name = json.loads(contest[6])['type']
	return render_template('contest.html',contest=contest,problems=problems,rule_name=rule_name)
