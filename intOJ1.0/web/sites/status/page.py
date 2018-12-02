from flask import *
from .recordlist import *

def Run():
	recordlist = Getrecordlist()
	return render_template('status.html',recordlist=recordlist)
