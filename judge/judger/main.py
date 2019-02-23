#coding:utf-8
import pymysql,redis
import time,os,json,math
from modules import *
import compile,run,judge
import db

cpppath = "../tmp/a.cpp"

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

casescore = []
def Getcasescore(cnt):
	global casescore
	casescore = []
	casescore.append(-1)
	left = 100
	per = 100//cnt
	for i in range(cnt-1):
		casescore.append(per)
		left -= per
	casescore.append(left)

while True:
	runid = Redis_Read()
	if runid == None:
		time.sleep(0.2)
		continue
	# redis_con.lpush('intoj-waiting',runid)

	runid = int(runid)
	print("\033[46;37mJudging runid:%d\033[0m"%runid)

	(problem_id,code,origin) = db.Readrecord(runid)
	db.Startjudge(runid)
	Writecode(code)
	(time_limit,memory_limit) = db.Readproblem(problem_id)
	output_limit = 65536

	comp_time_limit = 5000
	comp_memory_limit = 512
	comp_output_limit = 32768
	(comp_code,comp_message) = compile.Compile(comp_time_limit,comp_memory_limit,comp_output_limit)
	if( comp_code != 10 ):
		db.CompileError(runid,comp_message)
		time.sleep(1)
		continue

	filepath = "../testdata/%d/" % problem_id
	casecnt = int(  os.popen("cd %s;ls -l |grep \"^-\"|wc -l"%filepath).readline().strip() ) // 2
	Getcasescore(casecnt)

	subtasks = []
	for i in range(1,casecnt+1):
		nowstatus = 0
		if i == 1: nowstatus = 1
		subtasks.append({
			"id":i,
			"status":nowstatus,
			"score":0,
			"full_score":casescore[i],
			"time_usage":0,
			"memory_usage":0,
			"judger_message": '',
			"checker_message": ''
		})
	db.Report(runid,1,0,0,0,{'subtasks':subtasks},comp_message)

	tot_time_usage = tot_memory_usage = tot_score = 0
	final_status = 10
	for i in range(1,casecnt+1):
		inputfile = filepath + str(i) + ".in"
		outputfile = "../tmp/out.out"
		ansfile = filepath + str(i) + ".out"
		(status,time_usage,memory_usage,exitcode,judger_message) = run.Run(time_limit,memory_limit,output_limit,inputfile,outputfile)
		if status != 10:
			subtasks[i-1] = {
				"id":i,
				"status":status,
				"score":0,
				"full_score":casescore[i],
				"time_usage":time_usage,
				"memory_usage":memory_usage,
				"judger_message":judger_message,
				"checker_message":""
			}
		else:
			(status,score,checker_message) = judge.txtcompare.Compare(outputfile,ansfile,casescore[i])
			subtasks[i-1] = {
				"id":i,
				"status":status,
				"score":score,
				"full_score":casescore[i],
				"time_usage":time_usage,
				"memory_usage":memory_usage,
				"judger_message":judger_message,
				"checker_message":checker_message
			}
			tot_score += score
		tot_time_usage += time_usage
		tot_memory_usage = max(tot_memory_usage,memory_usage)
		final_status = min(final_status,status)
		if i != casecnt:
			subtasks[i]["status"] = 1
		db.Report(runid,1,tot_score,tot_time_usage,tot_memory_usage,{'subtasks':subtasks},comp_message)

	db.Report(runid,final_status,tot_score,tot_time_usage,tot_memory_usage,{'subtasks':subtasks},comp_message)

	time.sleep(1)
