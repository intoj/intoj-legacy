from flask import *
import pymysql
from ..modules import *

def Run():
	return render_template('login.html')
