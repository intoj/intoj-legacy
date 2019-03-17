from flask import *
import db,modules

def Run(problem_id):
	problem = db.Read_Problem(problem_id)

	submissions = db.Read_Submissions({'problem_id': problem_id, 'status': 10},'time_usage')
	submission_shown = []
	counted = {}
	for submission in submissions:
		if counted.get(submission[11]) != None: continue
		counted[submission[11]] = 1
		submission_shown.append(submission)
	return render_template('problem_ranklist.html',problem=problem,submissions=submission_shown)
