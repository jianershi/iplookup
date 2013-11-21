from flask import Flask, request, render_template
app = Flask(__name__)
from iplookup import *

def remote_addr(request):
    """
    Get the IP address of the visiting client

    gist source: https://gist.github.com/coreydowning/4099188

    :rtype: str
    :return: ip address
    """
    fwd = request.environ.get('HTTP_X_FORWARDED_FOR', None)
    if fwd is None:
        return request.environ.get('REMOTE_ADDR')
    # sometimes x-forwarded-for contains multiple addresses,
    # actual client is first, rest are proxy
    fwd = fwd.split(',')[0]
    return fwd

def processPage(jsonipdata):
    """
    Helper function to process longitude and latitude and render the page

    :type jsonipdata: str
    :param jsonipdata: json string
    """

    try:
        lon = json.loads(jsonipdata)['lon']
        lat = json.loads(jsonipdata)['lat']
    except KeyError:
        lon = None
        lat = None

    if (lon == None or lat == None):
        return render_template('iplookup.html', jsonipdata=jsonipdata)
    elif (lon != None and lat !=None):
        return render_template('iplookup.html', jsonipdata=jsonipdata, lon=lat, lat=lon)

@app.route('/')
def index():
    """default endpoint

    Listing the current vistor information
    """
    ipaddr = remote_addr(request)
    jsonipdata=iplookup(ipaddr);
    return processPage(jsonipdata)

@app.route('/<path:path>',methods=['GET'])
def apiHandler(path):
    """API endpoint

    Support /ipAddress and /domainName
    """
    ipaddr = path
    jsonipdata=iplookup(ipaddr);
    return processPage(jsonipdata)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
