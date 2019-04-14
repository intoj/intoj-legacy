#coding:utf-8
from flask import *
import db,modules

problem_per_page = 20

def Run():
	page = int(request.args['page']) if 'page' in request.args else 1

	problemlist = db.Read_Problemlist()

	can_view_hidden = modules.Current_User_Privilege(2)
	problem_show, total_page = modules.Page_Split( problemlist , page , problem_per_page ,
							lambda problem: problem['is_public'] or can_view_hidden )

	submitted_status = {}
	if modules.Is_Loggedin():
		def Better(new,before):
			if new['status'] != before['status']: return new['status'] > before['status']
			if new['score'] != before['score']: return new['score'] > before['score']
			if new['time_usage'] != before['time_usage']: return new['time_usage'] < before['time_usage']
			if new['memory_usage'] != before['memory_usage']: return new['memory_usage'] < before['memory_usage']
			if new['id'] != before['id']: return new['id'] > before['id']
			return False
		submissions = db.Read_Submissions({'username':request.cookies['username']},'id ASC')
		for submission in submissions:
			problem_id = submission['problem_id']
			if problem_id not in submitted_status or Better(submission,submitted_status[problem_id]):
				submitted_status[problem_id] = submission

	return render_template('problemlist.html',problemlist=problem_show,submitted_status=submitted_status,current_page=page,total_page=total_page)
