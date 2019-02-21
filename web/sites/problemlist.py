#coding:utf-8
from flask import *
import db,modules

def Run():
	problemlist = db.Read_Problemlist()
	return render_template('problemlist.html',problemlist=problemlist)
