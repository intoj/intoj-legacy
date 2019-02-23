#coding:utf-8
import os,subprocess,math

path = "../tmp"
exepath = "../tmp/a"
stderrpath = "../tmp/stderr.txt"

# 参数: timelim(ms),memlim(mb),outputlim(kb),inputpath,outputpath
# 返回: (type,time,memory,exitcode,message)
# 其中 type 为评测代码
def Run(timelim,memlim,outputlim,inputpath,outputpath):
	try:
		(status,_unused_mes) = subprocess.getstatusoutput(" \
		lrun \
		--max-real-time %f \
		--max-memory %d \
		--max-output %d \
		--network false \
		--syscalls 'write,open,close,read,exit,brk,fstat,mmap,mprotect,access,openat,execve,exit_group,arch_prctl,munmap' \
		./%s < %s 1> %s 2> %s \
		3>../tmp/result.txt \
		" % (timelim/1000.0,memlim*1024*1024,outputlim*1024,exepath,inputpath,outputpath,stderrpath) )		# TODO --max-nprocess
		# --max-nfile 2 \

		message = open("../tmp/result.txt",'r').read()
		# print(message)
		time = math.floor(float(message[message.find("CPUTIME"):message.find("REALTIME")][7:].strip())*1000)
		memory = round(int(message[:message.find("CPUTIME")][6:].strip())/1024/1024,2)
		exitcode = int(message[message.find("TERMSIG"):message.find("EXCEED")][8:].strip())
		exceed = message[message.find("EXCEED"):][6:].strip()

		if exceed == "OUTPUT":
			return(5,time,memory,exitcode,"Output Limit Exceed")
		if exceed == "REAL_TIME":
			return(6,time,memory,exitcode,"Time Limit Exceed")
		if exceed == "MEMORY":
			return(7,time,memory,exitcode,"Memory Limit Exceed")
		if exitcode != 0:
			return(8,time,memory,exitcode,"Runtime Error: signal %d"%exitcode)
		return (10,time,memory,exitcode,"")
	except Exception as err_message:
		return (2,0,0,0,"在运行时出现 Unknown♂Error:\n%s"%err_message)

if __name__ == '__main__':
	print(Run(1000,400,65536,"../tmp/in.in","../tmp/out.out"))
