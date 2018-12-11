import time,sys,os
import pymysql

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

		result = open("judger/result/result.txt","r")
		status = result.readlines()
		length = len(status)
		for i in range(len(status)):
			status[i] = status[i][0:len(status[i])-1]
		status[length-1] = status[length-1].split()
		print(status)
		cur.execute("UPDATE records SET status='%s' WHERE rid=%d;" % (status[length-2],rid) )
		cur.execute("UPDATE records SET score=%s WHERE rid=%d;" % (status[length-1][0],rid) )
		cur.execute("UPDATE records SET time=%s WHERE rid=%d;" % (status[length-1][1],rid) )
		cur.execute("UPDATE records SET memory=%s WHERE rid=%d;" % (status[length-1][2],rid) )
		db.commit()

	db.close()
	time.sleep(1)
