#coding:utf-8
from flask import *
import pymysql,redis
import db,modules,problem

#包含rejudge

def Submit(problemid,req,contest_id=0):
	code = req['code']
	if len(code) < 10:
		flash('这么短真的没问题?','error')
		return modules.Page_Back()

	runid = int(db.Fetchone("SELECT COUNT(*) FROM records;")[0]) + 1
	db.Execute("INSERT INTO records VALUES(%s,%s,%s,%s,0,0,'','{\"subtasks\":[]}',0,0,'',%s,%s);",(runid,problemid,code,'cpp',request.cookies['username'],contest_id))

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('intoj-waiting',str(runid))

	return redirect('/record/%d'%runid)

def Rejudge(id):
	if db.Fetchone("SELECT * FROM records WHERE id=%s",id) == None: return False

	db.Execute("UPDATE records SET status=0,score=0,result='{\"subtasks\":[]}',compilation='' WHERE id=%s",id)

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('intoj-waiting',str(id))

	return True
