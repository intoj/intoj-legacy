#coding:utf-8
from flask import *
import db,modules

def Run(contest_id):
	contest = db.Read_Contest(contest_id)
	if contest == None:
		flash('不存在的比赛','error')
		return modules.Page_Back()

	problems = json.loads(contest['problems'])
	problems = list(map( lambda x: db.Read_Problem(x['id']) , problems ))
	# print(problems)
	problems.sort( key = lambda x: x['id'] )

	ranklist = db.Read_Contest_Ranklist(contest_id)
	if ranklist == None:
		return render_template('contest_ranklist.html',contest=contest,ranklist=None)

	def Loadjson(x):
		if x['detail'] == '':
			x['detail'] = { 'score': 0, 'submit_cnt': 0 }
			return x
		x['detail'] = json.loads(x['detail'])
		score = submit_cnt = 0
		for problem_id_str,results in x['detail'].items():
			problem_id = int(problem_id_str)
			score += results['score']
			submit_cnt += results['submit_cnt']
		x['detail']['score'] = score
		x['detail']['submit_cnt'] = submit_cnt
		return x
	ranklist = list(map( Loadjson , ranklist ))
	ranklist.sort( key = lambda x: (-x['detail']['score'],x['detail']['submit_cnt']) )

	length = len(ranklist)
	for i in range(length):
		if i != 0 and ranklist[i]['detail']['score'] == ranklist[i-1]['detail']['score'] and ranklist[i]['detail']['submit_cnt'] == ranklist[i-1]['detail']['submit_cnt']:
			ranklist[i]['detail']['rank'] = ranklist[i-1]['detail']['rank']
		else:
			ranklist[i]['detail']['rank'] = i+1
	return render_template('contest_ranklist.html',contest=contest,ranklist=ranklist,problems=problems,full_score=len(problems)*100)
