#coding:utf-8
import time
import redis
import judge_main

def Redis_Read():
	global redis_con
	try:
		return redis_con.lpop('intoj-waiting')
	except:
		redis_con = redis.Redis(host='localhost',port=6379,decode_responses=True)
		return redis_con.lpop('intoj-waiting')

while True:
	runid = Redis_Read()
	if runid == None:
		time.sleep(0.2)
		continue
	# redis_con.lpush('intoj-waiting',runid)

	judge_main.Judge(runid)
