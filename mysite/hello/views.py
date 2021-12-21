from django.shortcuts import render
from django.http import HttpResponse
from django.utils.html import escape

# Create your views here.

def myview(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    response = HttpResponse()
    resp1 = 'In a view - the zap cookie value is '+str(oldval) + '<br>'
    if oldval:
        response.set_cookie('zap', int(oldval)+1)
    else:
        response.set_cookie('zap', 42)
    response.set_cookie('sakaicar', 42, max_age=1000)


    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp2 =  "\n view count="+str(num_visits)


    response.set_cookie('dj4e_cookie', '26dafde7', max_age=1000)
    response.write(resp1)
    response.write(resp2)
    return response