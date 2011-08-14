# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Url(models.Model):

    shortid = models.CharField(max_length=4, unique=True, null=True,
                               blank=True, verbose_name=_(u'Short ID'))
    url = models.URLField(unique=True, verbose_name=_(u'URL'))
    views = models.IntegerField(default=0, verbose_name=_(u'Views'))

    class Meta:
        verbose_name = _(u'URL')
        verbose_name_plural = _(u'URLs')

    def enc_id(self):
        """Returns the encoded id (base62)."""
        alphabet = ('0123456789abcdefghijklmnopqrstuvwxyz'
                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        base = len(alphabet)
        startid = 100000
        try:
            num = Url.objects.latest('id').id + startid
        except Url.DoesNotExist:
            num = startid
        arr = []
        while num:
            rem = num % base
            num = num // base
            arr.append(alphabet[rem])
        arr.reverse()
        return ''.join(arr)

    def save(self):
        if not self.shortid:
            self.shortid = self.enc_id()
        super(Url, self).save()
