from flask import *
import pymysql
import redis

"""
提交过程:
1. problem.html发出POST请求
2. app.py调用 sites.newsubmit.page.Submit(rid,record)
3. Submit()写入数据库
4. Submit()写入Redis
5. Submit()返回rid
6. app.py跳转到结果页
7. 移锅给后端
"""

def Toascii(code):
	a = ""
	for i in code:
		a += hex(ord(i)) + ' '
	return a

def Submit(problemid,request):
	ucode = Toascii(request['code']);

	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT COUNT(*) FROM records;")
	runid = int(cur.fetchone()[0])+1
	index = "{\"pid\": %d,\"status\": 0,\"score\": 0,\"time\": 0,\"memory\": 0,\"code\": \"%s\",\"subtask\": {},\"compilemessage\": \"\",\"checkermessage\": \"\" }" % (problemid,ucode)
	print(index)
	cmd = "INSERT INTO records VALUES(%d,'%s');" % (runid,index)
	cur.execute(cmd)

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('intoj-waiting',str(runid))

	db.commit()
	db.close()

	return runid
