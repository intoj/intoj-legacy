#coding:utf-8
from flask import *
from .problemlist import *

def Run():
	problemlist = Getproblemlist()
	return render_template('problemlist.html',problemlist=problemlist)
