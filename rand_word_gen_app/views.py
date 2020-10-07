from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

# Create your views here.

def re_direct(request):
    if 'count' in request.session:    
        request.session['count'] += 1
    else: 
        request.session['count'] = 1
    request.session['rand_word'] = get_random_string(14)
    return redirect ('random_word/')

def rand(request):
    return render(request, 'index.html')

def reset(request):
    request.session['count'] = 1
    request.session['rand_word'] = get_random_string(14)
    # return HttpResponse('reset works')
    return redirect ('/random_word/')
