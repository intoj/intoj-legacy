import json

config = {}
def Readfromfile(filename):
	global config
	with open(filename,'r') as config_file:
		s = config_file.read()
		config = json.loads(s)
