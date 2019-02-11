#coding:utf-8
from flask import *
from ..modules import *
from .read_database import *

def Run(id):
	uproblem = Getproblem(id)
	if uproblem == None:
		return render_template('error.html',message="题目P%d没找着!\n可能是因为编号不对."%id)
	return render_template("problemedit.html",uproblem=uproblem)

def Change(id,req):
	index = "`id`=%s,`title`='%s',`description`='%s',`input_format`='%s',`output_format`='%s',\
			`example`='%s',`limit_and_hint`='%s',`time_limit`=%s,`memory_limit`=%s" % \
			(req['id'],Raw(req['title']),Raw(req['description']),Raw(req['input_format']),Raw(req['output_format']),\
			Raw(req['example']),Raw(req['limit_and_hint']),Raw(req['time_limit']),Raw(req['memory_limit']))
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cmd = "UPDATE problems SET %s WHERE id=%d;" % (index,id)
	cur.execute(cmd)

	db.commit()
	db.close()

	return int(req['id'])
