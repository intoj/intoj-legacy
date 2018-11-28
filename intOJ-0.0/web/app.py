#export FLASK_ENV=development
import sys,time,os
from flask import *
app = Flask(__name__)

def Showsubmit():
	return render_template('submit.html')
def Submit(code):
	#print(code)
	codef = open("../judge/tmp/code.cpp","w")
	codef.write(code)
	codef.close()
	os.system('cp ../judge/tmp/code.cpp ../judge/Sy-judger/source/a+b.cpp')
	os.system('cd ../judge/Sy-judger && ./sy-judger')
	time.sleep(2)
	statf = open("../judge/Sy-judger/status.txt","r")
	stat = statf.read()
	print(stat)
	return render_template('result.html',code=code,stat=stat)
@app.route('/submit',methods=['GET','POST'])
def submit():
	if request.method == 'GET': return Showsubmit()
	return Submit(request.form['code'])
