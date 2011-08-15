# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.core.validators import URLValidator
from django.http import (HttpResponse, HttpResponseBadRequest,
                         HttpResponseForbidden, HttpResponseRedirect)
from django.shortcuts import get_object_or_404
from urlshortener.models import Url

def get_link(shortid, request):
    """Returns the full link of a shorten url."""
    path = reverse(open_shorturl, kwargs={'shortid': shortid})
    return 'http://%s%s' % (request.get_host(), path)

def open_shorturl(request, shortid):
    """Opens a short url."""
    url_obj = get_object_or_404(Url, shortid=shortid)
    # Update views
    url_obj.views += 1
    url_obj.save()
    return HttpResponseRedirect(url_obj.url)

def create_shorturl(request, secret):
    """Creates a short url."""
    if (not hasattr(settings, 'URLSHORTENER_SECRET')
        or secret != settings.URLSHORTENER_SECRET):
        return HttpResponseForbidden()
    url = request.GET.get('u') or ''
    if not url.startswith('http'):
        url = 'http://%s' % url
    validate = URLValidator(verify_exists=True)
    try:
        validate(url)
    except ValidationError:
        return HttpResponseBadRequest()
    try:
        url_obj = Url.objects.get(url=url)
    except Url.DoesNotExist:
        url_obj = Url(url=url)
        url_obj.save()
    return HttpResponse(get_link(url_obj.shortid, request))
