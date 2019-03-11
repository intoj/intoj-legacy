#coding:utf-8
from flask import *
import db,modules

def Useredit(username,req):
	db.Execute("UPDATE users SET `nameplate`=%s,`email`=%s,`sex`=%s,`group`=%s,`background_url`=%s WHERE username=%s;",(req['nameplate'],req['email'],req['sex'],req['group'],req['background_url'],username))

def Run(username):
	if username != request.cookies['username'] and not modules.Current_User_Privilege(1):
		flash(r'没有权限','error')
		return modules.Page_Back()
	userdata = db.Read_User_Byname(username)
	if userdata == None:
		flash(r'用户 %s 不存在'%username,'error')
		return modules.Page_Back()

	if request.method == 'GET':
		userdata = list(userdata)
		return render_template('useredit.html',user=userdata)
	else:
		Useredit(username,request.form)
		flash('修改成功','ok')
		return redirect('/user/%s'%username)
