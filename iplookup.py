import json
import requests

url="http://ip-api.com/json/"

def iplookup(ipaddr):
	"""
	Calls to http://ip-api.com/docs/ API

	:type ipaddr: str
	:param ipaddr: ip address
	:rtype: str
	:return: json string
	"""

	r=requests.get(url+ipaddr)
	return json.dumps(json.loads(r.content),indent=4)