from flask import *
from .problemlist import *
import json

def Fromascii(s):
	a = ""
	s = s.split()
	for i in s:
		a += chr(int(i,16))
	return a
def Run():
	prolist = Getproblemlist()
	problemlist = []
	for i in prolist:
		decoded = json.loads(i[1])
		decoded['pid'] = int(i[0])
		decoded['title'] = Fromascii(decoded['title'])
		problemlist.append(decoded)
	return render_template('problemlist.html',problemlist=problemlist)
