#coding:utf-8
from flask import *
import db,modules

def Run(contest_id):
	contest = db.Read_Contest(contest_id)
	if contest == None:
		flash('不存在的比赛','error')
		return modules.Page_Back()

	problems = json.loads(contest[8])
	problems = list(map( lambda x: db.Read_Problem(x['id']) , problems ))
	# print(problems)
	problems.sort( key = lambda x: x[0] )

	ranklist = db.Read_Contest_Ranklist(contest_id)
	if ranklist == None:
		return render_template('contest_ranklist.html',contest=contest,ranklist=None)

	def Loadjson(x):
		x = list(x)
		if x[3] == '':
			x[3] = { 'score': 0, 'submit_cnt': 0 }
			return x
		x[3] = json.loads(x[3])
		score = submit_cnt = 0
		for problem_id_str,results in x[3].items():
			problem_id = int(problem_id_str)
			score += results['score']
			submit_cnt += results['submit_cnt']
		x[3]['score'] = score
		x[3]['submit_cnt'] = submit_cnt
		return x
	ranklist = list(map( Loadjson , ranklist ))
	ranklist.sort( key = lambda x: (-x[3]['score'],x[3]['submit_cnt']) )

	length = len(ranklist)
	for i in range(length):
		if i != 0 and ranklist[i][3]['score'] == ranklist[i-1][3]['score'] and ranklist[i][3]['submit_cnt'] == ranklist[i-1][3]['submit_cnt']:
			ranklist[i][3]['rank'] = ranklist[i-1][3]['rank']
		else:
			ranklist[i][3]['rank'] = i+1
	return render_template('contest_ranklist.html',contest=contest,ranklist=ranklist,problems=problems,full_score=len(problems)*100)
