import config
import redis as pyredis

def Connect():
	redis_ip = config.config['redis']['ip']
	redis_port = config.config['redis']['port']
	redis_connection = pyredis.Redis(host=redis_ip,port=redis_port,decode_responses=True)
	return redis_connection
def End_Connect(redis_connection):
	# redis_connection.close()
	pass

def Rpush(queuename,value):
	redis_connection = Connect()
	redis_connection.rpush(queuename,value)
	End_Connect(redis_connection)
