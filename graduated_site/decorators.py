from django.http import HttpResponseBadRequest
from django.shortcuts import HttpResponseRedirect, reverse

def is_post(func):
    def wrap(request, *args, **kwargs):
        if request.method == 'GET':
            return HttpResponseBadRequest()
        return func(request, *args, **kwargs)
    return wrap

def anonymous_required(func):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
           return HttpResponseRedirect(reverse('home'))
        return func(request, *args, **kwargs)
    return wrap

