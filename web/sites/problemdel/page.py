#coding:utf-8
from flask import *
import pymysql
from ..modules import *

def Deleteproblem(pid):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	try:
		cur.execute("DELETE FROM problems WHERE id=%s",pid)
	except:
		flash(r'### 题目 P%d 没找着! \n 可能是因为编号不对.'%pid,'error')
		return redirect('/problemlist')
	db.commit()
	db.close()
	return redirect('/problemlist')
