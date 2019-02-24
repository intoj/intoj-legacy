#coding:utf-8
from flask import *
import pymysql,redis
import db,modules

#包含rejudge

def Submit(problemid,request,username,contest_id=0):
	code = request['code']
	if len(code) < 10:
		return -1,"这么短真的没问题?"

	runid = int(db.Fetchone("SELECT COUNT(*) FROM records;")[0]) + 1
	db.Execute("INSERT INTO records VALUES(%s,%s,%s,%s,0,0,'','{\"subtasks\":[]}',0,0,'',%s,%s);",(runid,problemid,code,'cpp',username,contest_id))

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('intoj-waiting',str(runid))

	return runid,""

def Rejudge(id):
	if db.Fetchone("SELECT * FROM records WHERE id=%s",id) == None: return False

	db.Execute("UPDATE records SET status=0,score=0,result='{\"subtasks\":[]}',compilation='' WHERE id=%s",id)

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('intoj-waiting',str(id))

	return True
