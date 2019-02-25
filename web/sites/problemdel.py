#coding:utf-8
from flask import *
import pymysql
import db,modules

def Deleteproblem(pid):
	try:
		db.Execute("DELETE FROM problems WHERE id=%s",pid)
	except:
		flash(r'### 题目 P%d 没找着! \n 可能是因为编号不对.'%pid,'error')
		return modules.Page_Back()
	return redirect('/problemlist')
