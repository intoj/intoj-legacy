#coding:utf-8
from flask import *
import db,modules

status_per_page = 15

def Submissions_My(contest_id):
	try: page = int(request.args['page'])
	except: page = 1

	if not modules.Is_Loggedin():
		flash(r'请先登录','error')
		return modules.Page_Back()

	contest = db.Read_Contest(contest_id)
	if contest == None:
		flash(r'不存在的比赛','error')
		return modules.Page_Back()

	limitations = request.args.to_dict()
	limitations['contest_id'] = contest_id
	limitations['username'] = modules.Current_User()
	submissions = db.Read_Submissions(limitations)
	print(submissions)
	status_show, total_page = modules.Page_Split( submissions , page , status_per_page ,
							lambda status: True )
	return render_template('status.html',statuslist=status_show,total_page=total_page,current_page=page,contest=contest,contest_id=contest_id,my=True)

def Submissions_All(contest_id):
	try: page = int(request.args['page'])
	except: page = 1

	contest = db.Read_Contest(contest_id)
	if contest == None:
		flash(r'不存在的比赛','error')
		return modules.Page_Back()

	limitations = request.args.to_dict()
	limitations['contest_id'] = contest_id
	submissions = db.Read_Submissions(limitations)

	status_show, total_page = modules.Page_Split( submissions , page , status_per_page ,
							lambda status: True )

	return render_template('status.html',statuslist=status_show,total_page=total_page,current_page=page,contest=contest,contest_id=contest_id,my=False)
