#coding:utf-8
import pymysql
import time,os,json
import db,modules
import compile,run,judge,read_testdata

cpppath = "../tmp/a.cpp"
output_limit = 65536
comp_time_limit = 5000
comp_memory_limit = 512
comp_output_limit = 32768
spj_comp_time_limit = 5000
spj_comp_memory_limit = 512
spj_comp_output_limit = 32768

def Judge(_runid):

	def Init_Judge():
		global problem, time_limit, memory_limit
		problem = db.Read_Problem(record['problem_id'])
		time_limit = problem['time_limit']
		memory_limit = problem['memory_limit']
		with open(cpppath,"w") as f:
			f.write(record['code'])

	def Compile():
		global comp_code, comp_message
		comp_code, comp_message = compile.Compile(comp_time_limit,comp_memory_limit,comp_output_limit)
		if comp_code != 10:
			db.Report(runid,status=comp_code,comp_message=comp_message)
			time.sleep(0.1)
			return False
		return True

	def Compile_Spj():
		if special_judge['compiled']: return
		spjpath = '../testdata/%d/%s' % (problem['id'],special_judge['name'])
		spj_exepath = '../testdata/%d/spj_compiled' % problem['id']
		comp_code, comp_message = compile.Compile( spj_comp_time_limit, spj_comp_memory_limit, spj_comp_output_limit, cpppath = spjpath, exepath = spj_exepath )
		if comp_code != 10:
			raise BaseException("spj compile error: %s"%comp_message)

	def Init_Subtasks():
		global subtasks, tot_time_usage, tot_memory_usage, tot_score, final_status
		subtasks = []
		for i in range(0,casecnt):
			subtasks.append({
				"id": i+1,
				"status": 1 if i == 0 else 0,
				"score": 0,
				"full_score": scores[i],
				"time_usage": 0,
				"memory_usage": 0,
				"judger_message": '',
				"checker_message": ''
			})
		tot_time_usage = tot_memory_usage = tot_score = 0
		final_status = 10

	def Runjudge(i):
		global subtasks, tot_time_usage, tot_memory_usage, tot_score, final_status
		inputfile = '../testdata/%d/%s' % (problem['id'],input_files[i])
		ansfile = '../testdata/%d/%s' % (problem['id'],answer_files[i])
		outputfile = '../tmp/user_output'
		status, time_usage, memory_usage, exitcode, judger_message = run.Run(time_limit,memory_limit,output_limit,inputfile,outputfile)
		if status != 10:
			subtasks[i] = {
				"id": i+1,
				"status": status,
				"score": 0,
				"full_score": scores[i],
				"time_usage": time_usage,
				"memory_usage": memory_usage,
				"judger_message": judger_message,
				"checker_message": ""
			}
		else:
			status, score, checker_message = Compare(inputfile,outputfile,ansfile,scores[i])
			subtasks[i] = {
				"id": i+1,
				"status": status,
				"score": score,
				"full_score": scores[i],
				"time_usage": time_usage,
				"memory_usage": memory_usage,
				"judger_message": judger_message,
				"checker_message": checker_message
			}
			tot_score += score
		tot_time_usage += time_usage
		tot_memory_usage = max(tot_memory_usage,memory_usage)
		final_status = min(final_status,status)
		if i != casecnt-1:
			subtasks[i+1]["status"] = 1

	def Compare(input_file,output_file,answer_file,fullscore):
		if special_judge['using'] == False:
			return judge.txtcompare.Compare(output_file,answer_file,fullscore)
		else:
			spj_exepath = '../testdata/%d/spj_compiled' % problem['id']
			return judge.special_judge.Special_Judge(input_file,output_file,answer_file,fullscore,spj_exepath)

	runid = int(_runid)
	print("\033[46;37mJudging runid:%d\033[0m"%runid)

	try:
		record = db.Read_Record(runid)
		Init_Judge()
		db.Startjudge(runid)

		compile_success = Compile()
		if not compile_success: return

		input_files, answer_files, scores, casecnt, special_judge = read_testdata.Read_Testdata("../testdata/%d/"%problem['id'])
		if special_judge['using'] == True:
			Compile_Spj()
		Init_Subtasks()
		db.Report(runid,1,0,0,0,{'subtasks':subtasks},comp_message)

		for i in range(0,casecnt):
			Runjudge(i)
			db.Report(runid,1,tot_score,tot_time_usage,tot_memory_usage,{'subtasks':subtasks},comp_message)

		db.Report(runid,final_status,tot_score,tot_time_usage,tot_memory_usage,{'subtasks':subtasks},comp_message)
		if record['contest_id'] != 0 and final_status >= 4:
			contest_player_info = db.Read_Contest_Player(record['username'],record['contest_id'])
			submit_cnt = 1 if str(problem['id']) not in contest_player_info else contest_player_info[str(problem['id'])]["submit_cnt"]+1
			contest_player_info[str(problem['id'])] = {
				"record_id": runid,
				"score": tot_score,
				"submit_cnt": submit_cnt
			}
			db.Save_Contest_Player(record['username'],record['contest_id'],contest_player_info)

		time.sleep(0.1)

	except Exception as error_message:
		print("\033[41;37mERROR!\033[0m",repr(error_message))
		db.Report(runid,system_message=repr(error_message))
		exit(0)
