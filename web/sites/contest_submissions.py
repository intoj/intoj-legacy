from flask import *
import db,modules

def Submissions_My(contest_id):
	if not modules.Is_Loggedin():
		flash(r'请先登录','error')
		return sites.modules.Page_Back()

	contest = db.Read_Contest(contest_id)
	if contest == None:
		flash(r'不存在的比赛','error')
		return modules.Page_Back()
	submissions = db.Read_Submissions({
		'contest_id': contest_id,
		'username': request.cookies['username']
	})
	return render_template('contest_submissions.html',statuslist=submissions,contest=contest,my=True)

def Submissions_All(contest_id):
	contest = db.Read_Contest(contest_id)
	if contest == None:
		flash(r'不存在的比赛','error')
		return modules.Page_Back()
	submissions = db.Read_Submissions({
		'contest_id': contest_id,
		'username': request.args.get('username'),
		'problem_id': request.args.get('problem_id')
	})
	return render_template('contest_submissions.html',statuslist=submissions,contest=contest,my=False)
