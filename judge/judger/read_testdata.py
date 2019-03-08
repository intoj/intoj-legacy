#coding: utf-8
import os

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

# 输入: filepath
# 返回: input_files[], answer_files[], scores[], casecnt
def Read_testdata(filepath):
	filelist = os.popen('cd %s;ls -1'%filepath).readlines()
	filelist = list(map(Compare_Key,filelist))
	if len(filelist) == 0: raise ValueError('没有测试数据')

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
	print(input_files)
	return input_files,answer_files,scores,casecnt

if __name__ == '__main__':
	# print(Compare_Key('test2333331.out'))
	print(Read_testdata('../testdata/10'))
