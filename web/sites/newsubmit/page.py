#coding:utf-8
from flask import *
import pymysql
import redis
from ..modules import *

#包含rejudge
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
	code = request['code']
	if len(code) < 10:
		return -1,"这么短真的没问题?"

	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT COUNT(*) FROM records;")
	runid = int(cur.fetchone()[0])+1

	cur.execute("INSERT INTO records VALUES(%s,%s,%s,%s,0,0,'','{\"subtasks\":[]}',0,0,'');",(runid,problemid,code,'cpp'))
	db.commit()
	db.close()

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('intoj-waiting',str(runid))

	return runid,""

def Rejudge(id):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT * FROM records WHERE id=%s",id)
	if cur.fetchone() == None: return False

	cur.execute("UPDATE records SET status=0,score=0,result='{\"subtasks\":[]}',compilation='' WHERE id=%s",id)
	db.commit()
	db.close()

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('intoj-waiting',str(id))

	return True
