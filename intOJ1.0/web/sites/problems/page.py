from flask import *
from .problemlist import *

def Run():
	prolist = Getproblemlist()
	return render_template('problems.html')
