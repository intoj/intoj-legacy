from flask import *
from .problemlist import *

def Run():
	prolist = Getproblemlist()
	return render_template('problemlist.html',prolist=prolist)
