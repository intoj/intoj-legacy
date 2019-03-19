#coding:utf-8
special_char = {
'\'': r'\'',
'\"': r'\"',
'\n': r'\n',
'\t': r'\t',
'\\': r'\\'
}
def Raw(origin):
	ans = ""
	for ch in origin:
		try: ans += special_char[ch]
		except: ans += ch
	return ans

import re
def Is_Number(num):
	pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
	result = pattern.match(num)
	if result:
		return True
	else:
		return False
