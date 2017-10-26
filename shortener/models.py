from django.db import models
from .utils import create_shortcode
import datetime

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

class KirrUrl(models.Model):

    # null = True -> Empty in Database is okay
    # blank = True -> Not required in Admin
    url         = models.CharField(max_length=220)
    shortcode   = models.CharField(max_length=15, unique = True, blank = True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    active      = models.BooleanField(default=True)

    objects = KirrUrlManager()

    # overwriting save method
    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == '':
            self.shortcode = create_shortcode(self)
        super(KirrUrl, self.save(*args, **kwargs))

    def __str__(self):
        return str(self.url)

    def __unicode__(self):
        return str(self.url)
