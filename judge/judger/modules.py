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
