#coding:utf-8
from flask import *
import hashlib,re
import db

tostatus = {
	0: "Waiting",
	1: "Running",
	2: "Unknown Error",
	3: "Compile Error",
	4: "Hacked",
	5: "Wrong Answer",
	6: "Time Limit Exceed",
	7: "Memory Limit Exceed",
	8: "Runtime Error",
	9: "Partially Accepted",
	10: "Accepted"
}
shortstatus = {
	0: "WJ",
	1: "Run",
	2: "UKE",
	3: "CE",
	4: "Hacked",
	5: "WA",
	6: "TLE",
	7: "MLE",
	8: "RE",
	9: "PAC",
	10: "AC"
}
statusicon = {
	0: "spinner icon-spin",
	1: "spinner icon-spin",
	2: "twitter",
	3: "github-alt",
	4: "magic",
	5: "remove",
	6: "time",
	7: "hdd",
	8: "asterisk",
	9: "adjust",
	10: "ok"
}
statuscolor = {
	0: '#888888',
	1: '#66ccff',
	2: '#aaaaaa',
	3: '#233333',
	4: '#ff4499',
	5: '#ff0000',
	6: 'orange',
	7: 'orange',
	8: 'purple',
	9: '#66ccff',
	10: '#00cc00'
}

def Score_Color(a,fullscore=100,opacity=1):
	a = float(a)
	fullscore = float(fullscore)
	if a <= fullscore/2:
		g = int( (a/fullscore) * (255+255-80) )
		return "rgb(255,%d,0,%f)" % (g,opacity) if opacity != 1 else "rgb(255,%d,0)" % g
	else:
		r = int( (1.0-a/fullscore) * (255+255) )
		return "rgb(%d,220,0,%f)" % (r,opacity) if opacity != 1 else "rgb(%d,220,0)" % r

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
def Is_Integer(str):
	return re.match(r'^-?[1-9]\d*$',str) != None or re.match(r'^-?0$',str) != None

def Get_Session(type,name):
	if session.get(type) == None:
		session[type] = {}
	return session[type].get(name)
def Set_Session(type,name,value):
	if session.get(type) == None:
		session[type] = {}
	session[type][name] = value
	session.update()

def Toint(x):
	return int(x) if int(x)==x else x
def Is_Loggedin():
	try:
		username = request.cookies['username']
		client_key = request.cookies['client_key']
		if Get_Session('client_keys',username) != client_key: return 0
		else: return 1
	except: return 0
def Current_User():
	if not Is_Loggedin(): return None
	return request.cookies.get('username')
def Current_User_Privilege(privilege_name):
	if not Is_Loggedin(): return 0
	return db.User_Privilege(request.cookies['username'],privilege_name)

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
def Argstring():
	arg = ""
	for key,value in request.args.items():
		if arg != "": arg += "&"
		arg += "%s=%s" % (Raw(key),Raw(value))
	return arg

def Page_Split(lst,page,per_page,condition):
	shown = []
	count = 0
	for now in lst:
		try:
			if condition(now):
				count += 1
				if per_page*(page-1) < count <= per_page*page: shown.append(now)
		except: pass
	total_page = count//per_page + ( 1 if count%per_page != 0 else 0 )
	return shown, total_page

def Todict(a):
	ret = {}
	for key,val in a.items():
		ret[key] = val
	return ret

def Default(val,default,invaild=None):
	return default if val == invaild else val
