from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# function based view - FBV
def kirr_redirect_view(request, *args, **kwargs):
    return HttpResponse("I'm from Function Based View!")

# class based view - CBV
class KirrCBView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse("I'm from Class Based View!")
