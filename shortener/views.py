from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrUrl

class HomeView(View):

    def get(self, request, *args, **kwargs):
        form = SubmitUrlForm()
        context = {
            'title': 'Submit URL',
            'form': form
        }
        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)

        context = {
            'title': 'Kirr.co',
            'form': form
        }

        template = 'shortener/home.html'

        if form.is_valid():
            new_url = form.cleaned_data.get('url')
            obj, created = KirrUrl.objects.get_or_create(url=new_url)
            context = {
                'object': obj,
                'created': created,
            }

            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already-exists.html'

        return render(request, template, context)

class KirrCBView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrUrl, shortcode=shortcode)
        return HttpResponse("{s}. I'm from Class Based View!".format(s=obj.url))
