from django.db import models

from shortener.models import KirrUrl

class ClickEventManager(models.Manager):

    def create_event(self, kirrInstance):
        if isinstance(kirrInstance, KirrUrl):
            obj, created = self.get_or_create(kirr_url=kirrInstance)
            obj.clicks += 1
            obj.save()
            return obj.clicks
        return None

class ClickEvent(models.Model):
    kirr_url    = models.OneToOneField(KirrUrl)
    clicks      = models.IntegerField(default = 0)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = ClickEventManager()

    def __str__(self):
        return '{i}'.format(i=self.clicks)

    def __unicode__(self):
        return '{i}'.format(i=self.clicks)
