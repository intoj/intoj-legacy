from flask import *
import json
import db,modules

def Run(id):
	contest = db.Read_Contest(id)
	problem_list = json.loads(contest[8])
	problems = []
	for problem in problem_list:
		problems.append(db.Read_Problem(problem['id']))
	rule_name = json.loads(contest[6])['type']
	return render_template('contest.html',contest=contest,problems=problems,rule_name=rule_name)
