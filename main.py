from flask import Flask, request, render_template
app = Flask(__name__)
from iplookup import *

def remote_addr(request):
    """
    The remote address of the client.
    gist source: https://gist.github.com/coreydowning/4099188
    """
    fwd = request.environ.get('HTTP_X_FORWARDED_FOR', None)
    if fwd is None:
        return request.environ.get('REMOTE_ADDR')
    # sometimes x-forwarded-for contains multiple addresses,
    # actual client is first, rest are proxy
    fwd = fwd.split(',')[0]
    return fwd

@app.route('/')
def index():
    ipaddr = remote_addr(request)
    jsonipdata=iplookup(ipaddr);
    return render_template('iplookup.html', jsonipdata=jsonipdata)

@app.route('/<path:path>',methods=['GET'])
def apiHandler(path):
	ipaddr = path
	jsonipdata=iplookup(ipaddr)
	return render_template('iplookup.html', jsonipdata=jsonipdata)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
