import pymysql
import redis
import time
import compile

r=redis.Redis(host='localhost',port=6379,decode_responses=True)

while True:
	#runid = r.lpop('intoj-waiting')
	#if runid == None: continue

	time.sleep(1)
