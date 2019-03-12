#coding:utf-8
from flask import *
import db,modules

def Run():
	contests = db.Read_Contestlist()
	return render_template('home.html',contests=contests)
