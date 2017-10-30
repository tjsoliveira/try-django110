from django.conf import settings
from django.db import models
from django.core.urlresolvers import reverse

from .utils import create_shortcode
from .validators import validate_url

class KirrUrlManager(models.Manager):

    def actives(self, *args, **kwargs):
        return super(KirrUrlManager, self).filter(active=True)

    def refresh_shortcodes(self):
        qs = KirrUrl.objects.filter(id__gte=1)
        new_codes = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_codes += 1
        return "New codes made: {i}".format(i=new_codes)

SHORTCODE_MAX = getattr(settings, 'SHORTCODE_MAX', 15)

class KirrUrl(models.Model):

    # null = True -> Empty in Database is okay
    # blank = True -> Not required in Admin
    url         = models.CharField(max_length=220, validators=[validate_url])
    shortcode   = models.CharField(max_length=SHORTCODE_MAX, unique = True, blank = True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)

    objects = KirrUrlManager()

    # overwriting save method
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(KirrUrl, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)

    def get_short_url(self):
        url_path = reverse('shortcode', kwargs={'shortcode': self.shortcode})
        return 'http://127.0.0.1:8000' + url_path
