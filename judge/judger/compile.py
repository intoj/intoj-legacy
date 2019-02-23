#coding:utf-8
import os,subprocess

path = "../tmp"
cpppath = "../tmp/a.cpp"
exepath = "../tmp/a"

# 参数: timelim(ms),memlim(mb),outputlim(kb)
# 返回: (type,message)
# 其中 type 为评测代码
def Compile(timelim,memlim,outputlim):
	try:
		(status,message) = subprocess.getstatusoutput(" \
		lrun \
		--max-real-time %f \
		--max-memory %d \
		--max-output %d \
		g++ -O2 -DONLINE_JUDGE %s -o %s -lm -w -fmax-errors=5 \
		3>&1 \
		" % (timelim/1000.0,memlim*1024*1024,outputlim*1024,cpppath,exepath) )

		exceed = message[message.find("EXCEED"):][6:].strip()
		if exceed == "REAL_TIME":
			return(3,"编译超时...你干了什么!?")
		if exceed == "MEMORY":
			return(3,"编译爆内存...但愿你不是在攻击")
		if exceed == "OUTPUT":
			return(3,"编译器输出了太多东西...建议本机编译一下试试")

		exitcode = int(message[message.find("EXITCODE"):message.find("TERMSIG")][8:].strip())
		if exitcode == 0:
			return(10,"")

		compmessage = message[:message.find("MEMORY")].strip()
		return (3,compmessage)
	except:
		return (2,"在编译时出现 Unknown♂Error")

if __name__ == '__main__':
	print(Compile(5000,256,65536))
