#coding:utf-8
import os, subprocess, math

# special judge
# 参数: inputpath, outputpath, anspath, fullscore, spj_exepath
# 返回值: status, score, message

spj_time_limit = 4000
spj_memory_limit = 512

def Special_Judge( inputpath, outputpath, anspath, fullscore, spj_exepath ):
	os.system('cp %s ../tmp/std_answer'%anspath)
	(status,_unused_mes) = subprocess.getstatusoutput(" \
		cd ../tmp && lrun \
		--max-real-time %f \
		--max-memory %d \
		--network false \
		 \
		./%s < %s 1> %s 2> %s \
		3>spj_result.txt \
	" % (spj_time_limit/1000.0,spj_memory_limit*1024*1024,spj_exepath,inputpath,'spj_output','spj_message') )
	with open('../tmp/spj_output','r') as spj_score_file:
		index = spj_score_file.readlines()
		try:
			index[0] = index[0].strip()
			index[1] = index[1].strip()
			status = int(index[0])
			score = float(index[1])/100 * fullscore
			if not index[1].isdigit(): raise ValueError()
		except:
			return 2, 0, 'spj 输出的分数不对: \n%s'%str(index)
	with open('../tmp/spj_message','r') as spj_message_file:
		message = spj_message_file.read()
	return status,score,message
