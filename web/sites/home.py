#coding:utf-8
from flask import *
import db,modules,config
import datetime

zisheng_delay_time = 3

def GET():
	contests = db.Read_Contestlist()
	users = list(db.Read_Userlist())
	users.sort( key = lambda x: (x['total_ac'],-x['total_submit']) , reverse=True )
	zishengs = db.Read_Zisheng()
	return render_template('home.html',contests=contests,users=users[:10],zishengs=zishengs)

def Send_Zisheng():
	if not modules.Is_Loggedin():
		flash('请先登录','error')
		return False

	message = request.form['message']
	max_length = config.config['site']['zisheng']['max_length']
	if len(message) > max_length:
		flash('超过最长长度: %d'%max_length,'error')
		return False

	username = request.cookies['username']
	last_zisheng_time = modules.Get_Session('last_zisheng_time',username)
	now_time = datetime.datetime.now()
	if last_zisheng_time != None:
		seconds = (now_time-last_zisheng_time).seconds
		if seconds < zisheng_delay_time:
			flash('请在 %ss 后提交'%(zisheng_delay_time-seconds),'error')
			return False
	modules.Set_Session('last_zisheng_time',username,now_time)

	nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	db.Execute("INSERT INTO zisheng VALUES(NULL,%s,%s,%s);",(username,request.form['message'],nowtime))

	flash('发送成功','ok')
	return True

def Run():
	if request.method == 'GET':
		return GET()
	else:
		is_success = Send_Zisheng()
		return redirect('/')
