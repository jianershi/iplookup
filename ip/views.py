# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.shortcuts import render_to_response, RequestContext
from datetime import tzinfo, timedelta, datetime
from django.views.decorators.csrf import csrf_exempt
from iplookup import iplookup

def index(request):
        return HttpResponse('index not defined');

def iplookup_views(request):
    ipaddr = request.META.get('REMOTE_ADDR', '')
#    print ipaddr
#    print type(ipaddr)
    jsonipdata=iplookup(ipaddr);
    context2={'jsonipdata':jsonipdata};
    return render(request,'ip/iplookup.html',context2);
