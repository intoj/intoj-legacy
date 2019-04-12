#coding:utf-8
from flask import *
import pymysql,redis,datetime
import db,modules,problem

#包含rejudge
submit_delay_time = 5

def Submit(problemid,req,contest_id=0):
	if not modules.Is_Loggedin():
		flash('请先登录','error')
		return modules.Page_Back()

	code = req['code']
	if len(code) < 10:
		flash('这么短真的没问题?','error')
		return modules.Page_Back()

	username = request.cookies['username']
	last_submit_time = modules.Get_Session('last_submit_time',username)
	now_time = datetime.datetime.now()

	if last_submit_time != None:
		seconds = (now_time-last_submit_time).seconds
		if seconds < submit_delay_time:
			flash('请在 %ss 后提交'%(submit_delay_time-seconds),'error')
			return modules.Page_Back()
	modules.Set_Session('last_submit_time',username,now_time)

	maxid_result = db.Fetchone("SELECT MAX(id) FROM records;")[0]
	runid = 1 if maxid_result == None else int(maxid_result) + 1
	nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	db.Execute("INSERT INTO records VALUES(%s,%s,%s,%s,0,0,'','{\"subtasks\":[]}',0,0,'',%s,%s,%s);",(runid,problemid,code,req['lang'],username,contest_id,nowtime))

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('intoj-waiting',str(runid))

	resp = make_response(redirect('/record/%d'%runid))
	resp.set_cookie('lastlang',req['lang'])
	return resp

def Rejudge(record_id):
	if db.Fetchone("SELECT * FROM records WHERE id=%s",record_id) == None:
		flash(r'提交记录R%d没找着!\\\n可能是因为编号不对.'%record_id,'error')
		return redirect('/status')

	db.Execute("UPDATE records SET status=0,score=0,time_usage=0,memory_usage=0,result='{\"subtasks\":[]}',compilation='' WHERE id=%s",record_id)

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('intoj-waiting',str(record_id))

	flash('成功重测.','ok')
	return redirect('/record/%d'%record_id)
