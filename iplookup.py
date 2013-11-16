import json
import requests

url="http://ip-api.com/json/"

def iplookup(ipaddr):
    r=requests.get(url+ipaddr)
    return json.dumps(json.loads(r.content),indent=4)