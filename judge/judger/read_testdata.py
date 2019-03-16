#coding: utf-8
import os, subprocess
import yaml

def Read_Testdata_Auto(filelist):
	def First_Appear(s,t):
		pos = -1
		for c in t:
			nowpos = s.find(c)
			if ( pos == -1 or nowpos < pos ) and nowpos != -1:
				pos = nowpos
		return pos
	def Compare_Key(s):
		s = s.strip()
		number_pos = First_Appear(s,'0123456789')
		if number_pos == -1: raise ValueError('文件名 %s 中没有一串连续的数字'%s)
		dot_pos = First_Appear(s[number_pos:],'.') + len(s[:number_pos])
		if dot_pos == -1: raise ValueError('文件名 %s 中没有\'.\''%s)

		file_prefix = s[:number_pos]
		file_caseid = int(s[number_pos:dot_pos])
		file_suffix = s[dot_pos:]
		return (file_prefix,file_caseid,file_suffix,s)
	def Get_Scores(cnt):
		scores = []
		left = 100
		per = 100//cnt
		for i in range(cnt-1):
			scores.append(per)
			left -= per
		scores.append(left)
		return scores

	filelist = list(map(Compare_Key,filelist))
	filelist.sort()
	file_prefix = filelist[0][0]
	for (nowfile_prefix,file_caseid,file_suffix,filename) in filelist:
		if file_prefix != nowfile_prefix:
			raise ValueError('文件名前缀不同: %s 与 %s'%(file_prefix,nowfile_prefix))

	casecnt = len(filelist) // 2
	scores = Get_Scores(casecnt)
	input_files = []
	answer_files = []
	for (file_prefix,file_caseid,file_suffix,filename) in filelist:
		if file_suffix == '.in': input_files.append(filename)
		else: answer_files.append(filename)
	special_judge = {
		'using': False
	}

	return input_files, answer_files, scores, casecnt, special_judge



def Read_Testdata_Yml(filepath,filelist):
	def Get_Scores(cnt):
		scores = []
		left = 100
		per = 100//cnt
		for i in range(cnt-1):
			scores.append(per)
			left -= per
		scores.append(left)
		return scores
	yamlpath = filepath + "/data.yml"
	config = yaml.safe_load(open(yamlpath,'r').read())

	input_format = config['input_file']
	answer_format = config['answer_file']
	input_files = []
	answer_files = []
	casecnt = len(config['subtasks'])
	scores = Get_Scores(casecnt)

	for task in config['subtasks']:
		input_files.append( input_format.replace('#',task) )
		answer_files.append( answer_format.replace('#',task) )

	special_judge = {
		'using': False
	}
	if config.get('special_judge') != None:
		spj_name = config['special_judge']
		if spj_name not in filelist:
			raise ValueError('没找到 Special Judge 文件: %s'%spj_name)

		spj_md5sum_now = os.popen('md5sum %s'%(filepath+'/'+spj_name)).read()
		if 'spj_compiled_md5sum' in filelist:
			spj_md5sum_before = open('%s/spj_compiled_md5sum'%filepath,'r').read()
		else:
			spj_md5sum_before = -1
		if spj_md5sum_now == spj_md5sum_before:
			spj_compiled = True
		else:
			open('%s/spj_compiled_md5sum'%filepath,'w').write(spj_md5sum_now)
			spj_compiled = False

		special_judge = {
			'using': True,
			'name': spj_name,
			'compiled': spj_compiled
		}

	return input_files, answer_files, scores, casecnt, special_judge



# 输入: filepath
# 返回: input_files[], answer_files[], scores[], casecnt, special_judge
# special_judge: {
# 	using: bool,
#	name: 'spj.cpp',
#	compiled: True
# }
def Read_Testdata(filepath):
	filelist = os.popen('cd %s;ls -1'%filepath).read().split()
	if len(filelist) == 0: raise ValueError('没有测试数据')

	if 'data.yml' in filelist: return Read_Testdata_Yml(filepath,filelist)
	else: return Read_Testdata_Auto(filelist)



if __name__ == '__main__':
	print(Read_Testdata('../testdata/1'))
