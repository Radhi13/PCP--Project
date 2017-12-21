# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 17:32:14 2017

@author: Radhika
The below code is used to test the httpresopnse and the Hello rquest.
this is not in the project
"""

from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world") 

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now        
    return HttpResponse(html)
