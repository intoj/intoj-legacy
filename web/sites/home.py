#coding:utf-8
from flask import *
import db,modules

def Run():
	contests = db.Read_Contestlist()

	users = list(db.Read_Userlist())[:10]
	users.sort( key = lambda x: x[9] , reverse=True )
	return render_template('home.html',contests=contests,users=users)
