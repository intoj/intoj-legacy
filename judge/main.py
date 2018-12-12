import time,sys,os
import pymysql

def GetFinalStatus(s):
	s = (s.split('\n'))[0:-1]
	length = len(s)
	status = s[length-2]
	ps = s[length-1].split()
	return (status,int(ps[0]),int(ps[1]),int(ps[2]))
def GetSubtaskStatus(s):
	s = (s.split('\n'))[0:-3]
	a = ""
	for i in s:
		a = a + '\n' + i
	return a

while(1):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM records WHERE status='Waiting'")
	res = cur.fetchone()
	if res != None:
		rid = res[0]
		cur.execute("UPDATE records SET status='Running' WHERE rid="+str(rid))
		db.commit()
		pid = res[1]
		cur.execute("SELECT * FROM problems WHERE pid="+str(pid))

		pres = cur.fetchone()
		tlim = pres[7]; mlim = pres[8]
		ctlim = 100000; cmlim = 256
		code = res[6]

		config = open("judger/tmp/config.txt","w")
		config.write("%d %d %d\n" % (pid,tlim,mlim))
		config.close()

		code = open("judger/judger/tmp/code.cpp","w")
		code.write(res[6])
		code.close()

		os.system("cd judger && ./judge")

		resultin = open("judger/result/result.txt","r")
		originstatus = resultin.read()
		(status,score,timeusage,memoryusage) = GetFinalStatus(originstatus)
		subtaskstatus = GetSubtaskStatus(originstatus)

		compileresultin = open("judger/judger/result/compileresult.txt","r")
		compileresult = compileresultin.read()
		cur.execute("UPDATE records SET status='%s' WHERE rid=%d;" % (status,rid) )
		cur.execute("UPDATE records SET score=%s WHERE rid=%d;" % (score,rid) )
		cur.execute("UPDATE records SET time=%s WHERE rid=%d;" % (timeusage,rid) )
		cur.execute("UPDATE records SET memory=%s WHERE rid=%d;" % (memoryusage,rid) )
		cur.execute("UPDATE records SET mes='%s' WHERE rid=%d;" % (compileresult,rid) )
		cur.execute("UPDATE records SET detail='%s' WHERE rid=%d;" % (subtaskstatus,rid) )
		db.commit()

	db.close()
	time.sleep(1)
