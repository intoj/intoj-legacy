#coding:utf-8
from flask import *
import db,modules

status_per_page = 15

def Run():
	args = dict(request.args)
	
	if args.get('contest_id') == None: args['contest_id'] = 0
	page = int(args['page']) if 'page' in args else 1

	statuslist = db.Read_Submissions(args)

	status_show, total_page = modules.Page_Split( statuslist , page , status_per_page ,
							lambda status: status[11] == modules.Current_User() or modules.Current_User_Privilege(2) or db.Read_Problem(status[1])[9] )

	if args['contest_id'] == 0:
		return render_template('status.html',statuslist=status_show,total_page=total_page,current_page=page,contest=None,contest_id=0)
	else:
		contest_id = args['contest_id']
		contest = db.Read_Contest(contest_id)
		return render_template('status.html',statuslist=status_show,total_page=total_page,current_page=page,contest=contest,contest_id=contest_id)
