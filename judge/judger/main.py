#coding:utf-8
import pymysql,redis
import time,os,json,math
from modules import *
import compile,run,judge,read_testdata
import db

cpppath = "../tmp/a.cpp"
output_limit = 65536
comp_time_limit = 5000
comp_memory_limit = 512
comp_output_limit = 32768

def Redis_Read():
	global redis_con
	try:
		return redis_con.lpop('intoj-waiting')
	except:
		redis_con = redis.Redis(host='localhost',port=6379,decode_responses=True)
		return redis_con.lpop('intoj-waiting')

def Writecode(code):
	f = open(cpppath,"w")
	f.write(code)
	f.close()

while True:
	runid = Redis_Read()
	if runid == None:
		time.sleep(0.2)
		continue
	# redis_con.lpush('intoj-waiting',runid)

	runid = int(runid)
	print("\033[46;37mJudging runid:%d\033[0m"%runid)

	try:
		record = db.Read_Record(runid)
		problem_id, code = record[1], record[2]
		db.Startjudge(runid)
		Writecode(code)
		problem = db.Read_Problem(problem_id)
		time_limit, memory_limit = problem[7], problem[8]

		(comp_code,comp_message) = compile.Compile(comp_time_limit,comp_memory_limit,comp_output_limit)
		if( comp_code != 10 ):
			db.Report(runid,status=comp_code,comp_message=comp_message)
			time.sleep(0.2)
			continue

		input_files, answer_files, scores, casecnt = read_testdata.Read_testdata("../testdata/%d/" % problem_id)
		print(input_files)

		subtasks = []
		for i in range(0,casecnt):
			nowstatus = 0
			if i == 0: nowstatus = 1
			subtasks.append({
				"id": i+1,
				"status": nowstatus,
				"score": 0,
				"full_score": scores[i],
				"time_usage": 0,
				"memory_usage": 0,
				"judger_message": '',
				"checker_message": ''
			})
		db.Report(runid,1,0,0,0,{'subtasks':subtasks},comp_message)

		tot_time_usage = tot_memory_usage = tot_score = 0
		final_status = 10
		for i in range(0,casecnt):
			inputfile = '../testdata/%d/%s' % (problem_id,input_files[i])
			ansfile = '../testdata/%d/%s' % (problem_id,answer_files[i])
			outputfile = "../tmp/out.out"
			(status,time_usage,memory_usage,exitcode,judger_message) = run.Run(time_limit,memory_limit,output_limit,inputfile,outputfile)
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
				(status,score,checker_message) = judge.txtcompare.Compare(outputfile,ansfile,scores[i])
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
			db.Report(runid,1,tot_score,tot_time_usage,tot_memory_usage,{'subtasks':subtasks},comp_message)

		db.Report(runid,final_status,tot_score,tot_time_usage,tot_memory_usage,{'subtasks':subtasks},comp_message)
		if record[12] != 0 and final_status >= 4:
			contest_player_info = db.Read_Contest_Player(record[11],record[12])
			submit_cnt = (1 if(str(problem_id) not in contest_player_info) else contest_player_info[str(problem_id)]["submit_cnt"]+1)
			contest_player_info[str(problem_id)] = {
				"record_id": runid,
				"score": tot_score,
				"submit_cnt": submit_cnt
			}
			db.Save_Contest_Player(record[11],record[12],contest_player_info)

		time.sleep(0.3)
	except Exception as error_message:
		print("\033[41;37mERROR!\033[0m",error_message)
		db.Report(runid,system_message=str(error_message))
		exit(0)
