from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views import View

from .models import KirrUrl

# function based view - FBV
def kirr_redirect_view(request, shortcode=None, *args, **kwargs):
    obj = get_object_or_404(KirrUrl, shortcode=shortcode)

    # obj_url = None
    # qs = KirrUrl.objects.filter(shortcode__iexact = shortcode)
    # if qs.exists():
    #   obj = qs.first()
    #   obj_url = qs.url

    return HttpResponse("{s}. I'm from Function Based View!".format(s=obj.url))

# class based view - CBV
class KirrCBView(View):

    def get(self, request, shortcode=None, *args, **kwargs):
        obj = get_object_or_404(KirrUrl, shortcode=shortcode)
        return HttpResponse("{s}. I'm from Class Based View!".format(s=obj.url))
