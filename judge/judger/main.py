import pymysql,redis
import time,os,json,math
from modules import *
import compile,run,judge

cpppath = "../tmp/a.cpp"

r=redis.Redis(host='localhost',port=6379,decode_responses=True)
db = pymysql.connect("localhost","intlsy","24","intoj")
cur = db.cursor()

def Readrecord(rid):
	cur.execute("SELECT * FROM records WHERE id=%d"%rid)
	dbresult = cur.fetchone()
	print("\033[42;37mRUNindex:\033[0m",dbresult)
	return dbresult[1],dbresult[2],dbresult
def Writecode(code):
	f = open(cpppath,"w")
	f.write(code)
	f.close()
def Startjudge(rid):
	cur.execute("UPDATE records SET status=1 WHERE id=%d" % rid)
	db.commit()

def Readproblem(problem_id):
	cur.execute("SELECT * FROM problems WHERE id=%d" % problem_id)
	dbresult = cur.fetchone()
	print("\033[42;37mPROindex:\033[0m",dbresult)
	return dbresult[7],dbresult[8]

def CompileError(runid,message):
	cur.execute("UPDATE records SET status=3 WHERE id=%d" % runid)
	cur.execute("UPDATE records SET compilation='%s' WHERE id=%d" % (Raw(message),runid))
	db.commit()

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

def Report(runid,status,score,time_usage,memory_usage,subtasks,comp_message):
	cur.execute("UPDATE records SET status=%d,score=%d,time_usage=%d,memory_usage=%d,result='%s',compilation='%s' WHERE id=%d" % \
				(status,score,time_usage,memory_usage,Raw(json.dumps(subtasks)),Raw(comp_message),runid))
	db.commit()

while True:
	runid = r.lpop('intoj-waiting')
	if runid == None: continue
	# r.lpush('intoj-waiting',runid)

	runid = int(runid)
	print("\033[46;37mJudging runid:%d\033[0m"%runid)

	(problem_id,code,origin) = Readrecord(runid)
	Startjudge(runid)
	Writecode(code)
	(time_limit,memory_limit) = Readproblem(problem_id)
	output_limit = 65536

	comp_time_limit = 5000
	comp_memory_limit = 512
	comp_output_limit = 32768
	(comp_code,comp_message) = compile.Compile(comp_time_limit,comp_memory_limit,comp_output_limit)
	if( comp_code != 10 ):
		CompileError(runid,comp_message)
		time.sleep(1)
		continue

	filepath = "../testdata/%d/" % problem_id
	casecnt = int(  os.popen("cd %s;ls -l |grep \"^-\"|wc -l"%filepath).readline().strip() ) // 2
	Getcasescore(casecnt)

	subtasks = []
	tot_time_usage = tot_memory_usage = tot_score = 0
	final_status = 10
	for i in range(1,casecnt+1):
		inputfile = filepath + str(i) + ".in"
		outputfile = "../tmp/out.out"
		ansfile = filepath + str(i) + ".out"
		(status,time_usage,memory_usage,exitcode,judger_message) = run.Run(time_limit,memory_limit,output_limit,inputfile,outputfile)
		if status != 10:
			subtasks.append({
				"id":i,
				"status":status,
				"score":0,
				"full_score":casescore[i],
				"time_usage":time_usage,
				"memory_usage":memory_usage,
				"judger_message":judger_message,
				"checker_message":""
			})
		else:
			(status,score,checker_message) = judge.txtcompare.Compare(outputfile,ansfile,casescore[i])
			subtasks.append({
				"id":i,
				"status":status,
				"score":score,
				"full_score":casescore[i],
				"time_usage":time_usage,
				"memory_usage":memory_usage,
				"judger_message":judger_message,
				"checker_message":checker_message
			})
			tot_score += score
		tot_time_usage += time_usage
		tot_memory_usage = max(tot_memory_usage,memory_usage)
		final_status = min(final_status,status)
	result = {
		'subtasks':subtasks
	}
	print("\033[42;37mSubtask:\033[0m",result)
	Report(runid,final_status,tot_score,tot_time_usage,tot_memory_usage,result,comp_message)

	time.sleep(1)
