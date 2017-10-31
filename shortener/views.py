from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View

from analytics.models import ClickEvent
from .forms import SubmitUrlForm
from .models import KirrUrl

class HomeView(View):

    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            'title': 'Kirr.co',
            'form': form,
        }
        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            'title': 'Kirr.co',
            'form': form,
        }

        template = 'shortener/home.html'

        if form.is_valid():
            template = 'shortener/detail.html'
            new_url = form.cleaned_data.get('url')
            obj, created = KirrUrl.objects.get_or_create(url=new_url)

            status = ''
            if created:
                status = 'The URL was Created'
            else:
                status = 'The URL already Exists'

            context = {
                'object': obj,
                'created': created,
                'status': status
            }

        return render(request, template, context)

class URLRedirectView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrUrl, shortcode=shortcode)
        ClickEvent.objects.create_event(obj)
        return HttpResponseRedirect(obj.url)
