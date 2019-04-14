import pymysql
from flask import *
import db,modules

def Total_Ac_Submit_Recalculate(username):
	print('Updating user %s'%username)
	total_ac = total_submit = 0
	ac_set = set()
	submissions = db.Read_Submissions({'username':username})
	for submission in submissions:
		status = submission['status']
		problem_id = submission['problem_id']
		total_submit += 1
		if status == 10:
			ac_set.add(problem_id)
	total_ac = len(ac_set)
	ac_list = json.dumps(list(ac_set))
	db.Execute('UPDATE users SET total_ac=%s, total_submit=%s, ac_list=%s WHERE username=%s',(total_ac,total_submit,ac_list,username))

def Total_Ac_Submit_Recalculate_All():
	userlist = db.Read_Userlist()
	for user in userlist:
		Total_Ac_Submit_Recalculate(user['username'])

if __name__ == '__main__':
	Total_Ac_Submit_Recalculate_All()
