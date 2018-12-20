import pymysql,redis
import time,os,json,math
import compile,run,judge
def Fromascii(s):
	a = ""
	s = s.split()
	for i in s:
		a += chr(int(i,16))
	return a
def Toascii(code):
	a = ""
	for i in code:
		a += hex(ord(i)) + ' '
	return a

cpppath = "../tmp/a.cpp"

r=redis.Redis(host='localhost',port=6379,decode_responses=True)
db = pymysql.connect("localhost","intlsy","24","intoj")
cur = db.cursor()

def Readrecord(rid):
	cur.execute("SELECT * FROM records WHERE rid=%d"%runid)
	dbresult = cur.fetchone()
	indexjson = dbresult[1]
	index = json.loads(indexjson)
	print("\033[42;37mRUNindex:\033[0m",index)
	pid = index['pid']
	code = Fromascii(index['code'])
	return pid,code,index
def Writecode(code):
	f = open(cpppath,"w")
	f.write(code)
	f.close()

def Readproblem(pid):
	cur.execute("SELECT * FROM problems WHERE pid=%d"%pid)
	dbresult = cur.fetchone()
	indexjson = dbresult[1]
	index = json.loads(indexjson)
	print("\033[42;37mPROindex:\033[0m",index)
	return index['timelimit'],index['memorylimit']

def CompileError(rid,mes,origin):
	origin['status'] = 3
	origin['compilemessage'] = Toascii(mes)
	cur.execute("UPDATE records SET content='%s' WHERE rid=%d" % (json.dumps(origin),rid))
	db.commit()

casescore = []
def Getcasescore(cnt):
	global casescore
	casescore = []
	casescore.append(23333)
	left = 100
	per = 100//cnt
	for i in range(cnt-1):
		casescore.append(per)
		left -= per
	casescore.append(left)

def Report(rid,status,score,time,mem,subtask,compmes,origin):
	origin['status'] = status
	origin['score'] = score
	origin['time'] = time
	origin['memory'] = mem
	origin['subtask'] = subtask
	origin['compilemessage'] = Toascii(compmes)
	print("\033[42;37mResult:\033[0m",origin)
	cur.execute("UPDATE records SET content='%s' WHERE rid=%d" % (json.dumps(origin),rid))
	db.commit()

while True:
	runid = r.lpop('intoj-waiting')
	if runid == None: continue
	# r.lpush('intoj-waiting',runid)

	runid = int(runid)
	print("\033[46;37mJudging runid:%d\033[0m"%runid)

	(pid,code,origin) = Readrecord(runid)
	Writecode(code)
	(timelim,memlim) = Readproblem(pid)
	outputlim = 65536

	comptimelim = 5000
	compmemlim = 512
	compoutputlim = 32768
	(compcode,compmes) = compile.Compile(comptimelim,compmemlim,compoutputlim)
	if( compcode != 10 ):
		CompileError(runid,compmes,origin)
		time.sleep(1)
		continue

	filepath = "../testdata/%d/" % pid
	casecnt = int(  os.popen("cd %s;ls -l |grep \"^-\"|wc -l"%filepath).readline().strip() ) // 2
	Getcasescore(casecnt)

	subtask = {}
	tottimeuse = totmemuse = totscore = 0
	finalstatus = 11
	for i in range(1,casecnt+1):
		inputfile = filepath + str(i) + ".in"
		outputfile = "../tmp/out.out"
		ansfile = filepath + str(i) + ".out"
		(status,timeuse,memuse,exitcode,judgermessage) = run.Run(timelim,memlim,outputlim,inputfile,outputfile)
		if status != 10:
			subtask[str(i)] = {
				"status":status,
				"score":0,
				"fullscore":casescore[i],
				"time":timeuse,
				"memory":memuse,
				"judgermessage":Toascii(judgermessage),
				"checkermessage":Toascii("Skipped")
			}
		else:
			(status,score,checkermessage) = judge.txtcompare.Compare(outputfile,ansfile,casescore[i])
			subtask[str(i)] = {
				"status":status,
				"score":score,
				"fullscore":casescore[i],
				"time":timeuse,
				"memory":memuse,
				"judgermessage":Toascii(judgermessage),
				"checkermessage":Toascii(checkermessage)
			}
			totscore += score
		tottimeuse += timeuse
		totmemuse = max(totmemuse,memuse)
		finalstatus = min(finalstatus,status)

	print("\033[42;37mSubtask:\033[0m",subtask)
	Report(runid,finalstatus,totscore,tottimeuse,totmemuse,subtask,compmes,origin)

	time.sleep(1)
