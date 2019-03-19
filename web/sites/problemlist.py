#coding:utf-8
from flask import *
import db,modules

problem_per_page = 20

def Run():
	page = int(request.args['page']) if 'page' in request.args else 1

	problemlist = db.Read_Problemlist()

	can_view_hidden = modules.Current_User_Privilege(2)
	problem_show, total_page = modules.Page_Split( problemlist , page , problem_per_page ,
							lambda problem: problem[9] or can_view_hidden )

	submitted_status = {}
	if modules.Is_Loggedin():
		def Better(new,before):
			if new[4] != before[4]: return new[4] > before[4]
			if new[5] != before[5]: return new[5] > before[5]
			if new[8] != before[8]: return new[8] < before[8]
			if new[9] != before[9]: return new[9] < before[9]
			if new[0] != before[0]: return new[0] > before[0]
			return False
		submissions = db.Read_Submissions({'username':request.cookies['username']},'id ASC')
		for submission in submissions:
			problem_id = submission[1]
			if problem_id not in submitted_status or Better(submission,submitted_status[problem_id]):
				submitted_status[problem_id] = submission

	return render_template('problemlist.html',problemlist=problem_show,submitted_status=submitted_status,current_page=page,total_page=total_page)
