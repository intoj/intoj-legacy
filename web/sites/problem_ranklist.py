from flask import *
import db,modules

status_per_page = 15

def Run(problem_id):
	problem = db.Read_Problem(problem_id)

	args = request.args
	page = int(args['page']) if 'page' in args else 1
	order = args['order'] if 'order' in args else 'time_usage'

	submissions = db.Read_Submissions({'problem_id': problem_id, 'status': 10},order)
	submission_shown = []
	counted = {}
	for submission in submissions:
		if counted.get(submission[11]) != None: continue
		counted[submission[11]] = 1
		submission_shown.append(submission)

	submission_shown_inpage, total_page = modules.Page_Split( submission_shown , page , status_per_page ,
							lambda status: True )

	return render_template('problem_ranklist.html',problem=problem,submissions=submission_shown_inpage,total_page=total_page,current_page=page)
