#coding:utf-8
from flask import *
import hashlib,re
import db

tostatus = {
	0:"Waiting",
	1:"Running",
	2:"Unknown Error",
	3:"Compile Error",
	4:"Hacked",
	5:"Wrong Answer",
	6:"Time Limit Exceed",
	7:"Memory Limit Exceed",
	8:"Runtime Error",
	9:"Partially Accepted",
	10:"Accepted"
}
statusicon = {
	0:"spinner icon-spin",
	1:"spinner icon-spin",
	2:"thumbs-down",
	3:"github-alt",
	4:"magic",
	5:"remove",
	6:"time",
	7:"hdd",
	8:"asterisk",
	9:"legal",
	10:"ok"
}
def Score_Color(a,fullscore=100):
	if a <= fullscore/2:
		g = int( (a/fullscore) * (255+255-80) )
		return "rgb(255,%d,0)" % g
	else:
		r = int( (1.0-a/fullscore) * (255+255) )
		return "rgb(%d,220,0)" % r

special_char = {
'\'': r'\'',
'\"': r'\"',
'\n': r'\n',
'\t': r'\t',
'\\': r'\\'
}
def Raw(origin):
	ans = ""
	for ch in origin:
		try: ans += special_char[ch]
		except: ans += ch
	return ans

def Email_Hash(s):
	return hashlib.md5(s.strip().lower().encode('utf-8')).hexdigest()
def Vaild_Username(username):
	return re.match(r'[A-Za-z0-9_\-]+',username) != None and re.match(r'[A-Za-z0-9_\-]+',username).span()[1] == len(username)

def Toint(x):
	return int(x) if int(x)==x else x
def Is_Loggedin():
	try:
		username = request.cookies['username']
		client_key = request.cookies['client_key']
		if session.get(username) != client_key: return 0
		else: return 1
	except: return 0
def Current_User_Privilege(id):
	if not Is_Loggedin(): return 0
	return db.User_Privilege(request.cookies['username'],id)

def Judge_Status(status):
	status = int(status)
	html = """
	<span class="judge-%d">
		<i class="icon-%s"> </i>
		%s
	</span> """ % (status,statusicon[status],tostatus[status])
	return html

def Referrer():
	return '/' if request.referrer == None else request.referrer
def Page_Back():
	return redirect(Referrer())
