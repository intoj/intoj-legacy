#coding:utf-8
from flask import *
import db,modules

def Run():
	contests = db.Read_Contestlist()

	users = list(db.Read_Userlist())
	users.sort( key = lambda x: (x[9],-x[10]) , reverse=True )
	return render_template('home.html',contests=contests,users=users[:10])
