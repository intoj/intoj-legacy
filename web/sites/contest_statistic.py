from flask import *
import db,modules,operator

def Run(contest_id):
	contest = db.Read_Contest(contest_id)
	submissions = db.Read_Submissions({
		'contest_id': contest_id
	})

	groups = {}
	for submission in submissions:
		user = db.Read_User_Byname(submission[11])
		group = user[7]
		if group == None or group.strip() == '': continue
		if groups.get(group) == None:
			groups[group] = {
				'tot_score_all': 0,
				'tot_submit_all': 0,
				'average_score_all': 0,
				'tot_score_finally': 0,
				'tot_submit_finally': 0,
				'average_score_finally': 0
			}
		groups[group]['tot_score_all'] += submission[5]
		groups[group]['tot_submit_all'] += 1
		groups[group]['average_score_all'] = round( groups[group]['tot_score_all'] / groups[group]['tot_submit_all'] , 2 )

	problems = {}
	for submission in submissions:
		problem = db.Read_Problem(submission[1])
		if problem == None: continue
		problem_id = problem[0]
		if problems.get(problem_id) == None:
			problems[problem_id] = {
				'tot_submit_all': 0,
				'tot_score_all': 0,
				'average_score_all': 0,
				'status_cnt_all': [ 0 for i in range(13) ],
				'tot_submit_finally': 0,
				'tot_score_finally': 0,
				'average_score_finally': 0,
				'status_cnt_finally': [ 0 for i in range(13) ],
				'name': problem[1]
			}
		problems[problem_id]['tot_submit_all'] += 1
		problems[problem_id]['tot_score_all'] += submission[5]
		problems[problem_id]['status_cnt_all'][submission[4]] += 1
		problems[problem_id]['average_score_all'] = round( problems[problem_id]['tot_score_all'] / problems[problem_id]['tot_submit_all'] , 2 )
	problems = dict(sorted(problems.items(),key=operator.itemgetter(0)))

	players = db.Read_Contest_Ranklist(contest_id)
	for player in players:
		details = json.loads(player[3])
		for problem_id,detail in details.items():
			problem_id = int(problem_id)
			if problems.get(problem_id) == None: continue
			record = db.Read_Record(detail['record_id'])
			if record == None: continue
			problems[problem_id]['tot_submit_finally'] += 1
			problems[problem_id]['tot_score_finally'] += record[5]
			problems[problem_id]['status_cnt_finally'][record[4]] += 1
			problems[problem_id]['average_score_finally'] = round( problems[problem_id]['tot_score_finally'] / problems[problem_id]['tot_submit_finally'] , 2 )

		for problem_id,detail in details.items():
			record = db.Read_Record(detail['record_id'])
			if record == None: continue
			user = db.Read_User_Byname(player[1])
			group = user[7]
			if group == None or group.strip() == '': continue
			if groups.get(group) == None: continue
			groups[group]['tot_submit_finally'] += 1
			groups[group]['tot_score_finally'] += record[5]
			groups[group]['average_score_finally'] = round( groups[group]['tot_score_finally'] / groups[group]['tot_submit_finally'] , 2 )
			
	return render_template('contest_statistic.html',contest=contest,groups=groups,problems=problems)
