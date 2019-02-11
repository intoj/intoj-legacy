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
		return render_template('error.html',message="题目 P%d 没找着!\n可能是编号不对"%pid)
	db.commit()
	db.close()
	return redirect('/problemlist')
