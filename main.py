from flask import Flask, request, render_template
app = Flask(__name__)
from iplookup import *

@app.route('/')
def index():
    ipaddr = request.environ['REMOTE_ADDR']
    jsonipdata=iplookup(ipaddr);
    return render_template('iplookup.html', jsonipdata=jsonipdata)

@app.route('/<path:path>',methods=['GET'])
def apiHandler(path):
	ipaddr = path
	jsonipdata=iplookup(ipaddr)
	return render_template('iplookup.html', jsonipdata=jsonipdata)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
