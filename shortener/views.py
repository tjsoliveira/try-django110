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
        # if form.is_valid():
        #     print(form.cleaned_data)

        context = {
            'title': 'Submit URL',
            'form': form
        }
        return render(request, 'shortener/home.html', context)

class KirrCBView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrUrl, shortcode=shortcode)
        return HttpResponse("{s}. I'm from Class Based View!".format(s=obj.url))
