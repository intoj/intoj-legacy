from flask import *
from .problemlist import *
import json

def Run():
	prolist = Getproblemlist()
	problemlist = []
	for i in prolist:
		decoded = json.loads(i[1])
		decoded['pid'] = int(i[0])
		problemlist.append(decoded)
	return render_template('problemlist.html',problemlist=problemlist)
