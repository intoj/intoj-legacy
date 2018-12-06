import time,sys,os
import pymysql

db = pymysql.connect("localhost","intlsy","24","intoj")
cur = db.cursor()

while(1):
	cur.execute("SELECT * FROM records WHERE status='waiting';")
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
		config = open("judger/judgeconf.txt","w")
		config.write("%d %d %d %d %d\n" % (pid,tlim,mlim,ctlim,cmlim))
		config.close()

		code = open("judger/code.cpp","w")
		code.write(res[6])
		code.close()
	time.sleep(1)
	break

db.close()
