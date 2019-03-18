#coding:utf-8
from flask import *
import db,modules

def Run():
	contestlist = db.Read_Contestlist()
	return render_template('contestlist.html',contestlist=contestlist)
