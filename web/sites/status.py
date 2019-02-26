#coding:utf-8
from flask import *
import db,modules

def Run():
	statuslist = db.Read_Submissions(request.args)
	return render_template('status.html',statuslist=statuslist)
