from flask import *
import db,modules

def Run(problem_id):
	problem = db.Read_Problem(problem_id)

	submissions = db.Read_Submissions({'problem_id': problem_id})
	score_count = {}
	status_count = [ 0 for i in range(12) ]
	for submission in submissions:
		if submission['contest_id'] != 0: continue
		status_count[submission['status']] += 1
		if submission['status'] >= 4:
			score_count[submission['score']] = 1 if submission['score'] not in score_count else score_count[submission['score']] + 1
	score_count = sorted(score_count.items())
	return render_template('problem_statistic.html',problem=problem,score_count=score_count,status_count=status_count)
