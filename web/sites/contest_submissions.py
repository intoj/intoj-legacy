from flask import *
import db,modules

def Submissions_My(contest_id):
	contest = db.Read_Contest(contest_id)
	if contest == None:
		flash('不存在的比赛','error')
		return modules.Page_Back()
	submissions = db.Read_Contest_Submissions(contest_id,request.cookies['username'])
	return render_template('contest_submissions.html',statuslist=submissions,contest=contest)
