# 纯文本比较
# 忽略行首行末换行及空格
# 参数: outputpath,anspath,fullscore
# 返回值: status,score,message
def Compare(optpath,anspath,fullscore):
	try: optf = open(optpath,"r")
	except: return 2,0,"Can not open out file:%s"%optpath
	try: ansf = open(anspath,"r")
	except: return 2,0,"Can not open ans file:%s"%anspath

	opt = optf.readlines()
	ans = ansf.readlines()

	if len(opt) < len(ans): return 5,0,"Too few line: %d in ans but %d in yours." % (len(ans),len(opt))
	if len(opt) > len(ans): return 5,0,"Too many line: %d in ans but %d in yours." % (len(ans),len(opt))

	length = len(ans)
	for i in range(length):
		if opt[i].strip() == ans[i].strip(): continue
		o = opt[i].strip().split()
		a = ans[i].strip().split()
		if len(o) < len(a): return 5,0,"Too few things: at line %d, %d in ans but %d in yours." % (i+1,len(a),len(o))
		if len(o) > len(a): return 5,0,"Too many things: at line %d, %d in ans but %d in yours." % (i+1,len(a),len(o))
		ul = len(o)
		for j in range(ul):
			o[j] = o[j].strip()
			a[j] = a[j].strip()
			vl = len(o[j])
			for k in range(vl):
				if o[j][k] != a[j][k]:
					return 5,0,"Wrong Answer: at line %d element %d, %s in ans but %s found." % (i+1,j+1,a[j][k],o[j][k])

	return 10,fullscore,"Accepted.Congratulations!"

if __name__ == '__main__':
	print(Compare("../../testdata/0/1.out","../../testdata/0/2.out",100))
