from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .models import KirrUrl

class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'shortener/home.html', {})

class KirrCBView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrUrl, shortcode=shortcode)
        return HttpResponse("{s}. I'm from Class Based View!".format(s=obj.url))
