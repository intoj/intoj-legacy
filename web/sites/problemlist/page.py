from flask import *
from .problemlist import *

def Run():
	problemlist = Getproblemlist()
	for u in problemlist:
		print(u)
	return render_template('problemlist.html',problemlist=problemlist)
