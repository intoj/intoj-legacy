#export FLASK_ENV=development
from flask import *
import sys,time
import sites
app = Flask(__name__)

@app.route('/')
def Home():
	return sites.home.page.Run()
@app.route('/help')
def Help():
	return sites.help.page.Run()
