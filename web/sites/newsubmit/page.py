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

def Submit(problemid,request):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT COUNT(*) FROM records;")
	runid = int(cur.fetchone()[0])+1
	index = "%d,%d,'%s','%s',0,0,'','{\"subtasks\":[]}',0,0" % (runid,problemid,request['code'],'cpp')
	print(index)

	cmd = "INSERT INTO records VALUES(%s);" % index
	cur.execute(cmd)

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('intoj-waiting',str(runid))

	db.commit()
	db.close()

	return runid
