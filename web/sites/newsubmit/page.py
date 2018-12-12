from flask import *
import pymysql
import redis

"""
提交过程:
1. problem.html发出POST请求
2. app.py调用 sites.newsubmit.page.Submit(rid,record)
3. Submit()写入数据库
4. Submit()写入Redis
5. Submit()返回rid
6. app.py跳转到结果页
7. 移锅给后端
"""

specialc = ['\\','\'','\"']
def Tran(code):
	a = ""
	for i in code:
		if i in specialc:
			a += '\\'
			a += i
		else:
			a += i
	return a

def Submit(pid,req):
	db = pymysql.connect("localhost","intlsy","24","intoj")
	cur = db.cursor()
	cur.execute("SELECT COUNT(*) FROM records;")
	rid = int(cur.fetchone()[0])+1
	code = Tran(req['code']);
	cmd = "INSERT INTO records VALUES(%d,%d,'Waiting',0,0,0,'%s','');" % (rid,pid,code)
	cur.execute(cmd)

	r=redis.Redis(host='localhost',port=6379,decode_responses=True)
	r.rpush('judgelist',str(rid))

	db.commit()
	db.close()

	return rid

"""
#include<iostream>
using namespace std;

int main(){
	return 0;
}
"""
