from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# function based view - FBV
def kirr_redirect_view(request, slug=None, *args, **kwargs):
    print(slug)
    return HttpResponse("{s}. I'm from Function Based View!".format(s=slug))

# class based view - CBV
class KirrCBView(View):

    def get(self, request, slug=None, *args, **kwargs):
        print(slug)
        return HttpResponse("{s}. I'm from Class Based View!".format(s=slug))
