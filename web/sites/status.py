#coding:utf-8
from flask import *
import db,modules

def Run():
	statuslist = list(db.Read_Recordlist())
	return render_template('status.html',statuslist=statuslist)
