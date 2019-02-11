#coding:utf-8
import hashlib,re

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
def Color(a,fullscore=100):
	if a < fullscore*0.3: return "red"
	if a < fullscore*0.6: return "orange"
	if a < fullscore: return "forestgreen"
	return "#00ee00"

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
