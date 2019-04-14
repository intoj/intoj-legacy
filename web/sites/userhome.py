#coding:utf-8
from flask import *
import db,modules

def User_Statistic(username):
	submissions = db.Read_Submissions({'username':username})
	status_cnt = [ 0 for i in range(13) ]
	for submission in submissions:
		status_cnt[submission['status']] += 1
	return status_cnt

def Run(username):
	user = db.Read_User_Byname(username)
	if user == None:
		flash('用户 %s 不存在'%username,'error')
		return modules.Page_Back()

	status_cnt = User_Statistic(username)
	return render_template('userhome.html',user=user,status_cnt=status_cnt)
