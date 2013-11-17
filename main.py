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

def processPage(jsonipdata):
    try:
        lon = json.loads(jsonipdata)['lon']
        lat = json.loads(jsonipdata)['lat']
    except KeyError:
        lon = None
        lat = None

    try:
        from config import mapid
        try:
            if mapid == None:
                mapid = 'examples.map-9ijuk24y'
        except UnboundLocalError:
            mapid = 'examples.map-9ijuk24y'
    except ImportError:
        mapid = 'examples.map-9ijuk24y'

    if (lon == None or lat == None):
        return render_template('iplookup.html', jsonipdata=jsonipdata)
    elif (lon != None and lat !=None):
        return render_template('iplookup.html', jsonipdata=jsonipdata, lon=lat, lat=lon, mapid=mapid)

@app.route('/')
def index():
    ipaddr = remote_addr(request)
    jsonipdata=iplookup(ipaddr);
    return processPage(jsonipdata)

@app.route('/<path:path>',methods=['GET'])
def apiHandler(path):
    ipaddr = path
    jsonipdata=iplookup(ipaddr);
    return processPage(jsonipdata)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
