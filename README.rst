django-urlshortener
===================

A simple URL shortener for your Django project.

Prerequisites
=============

  * Django

Installation
============

pip install -e git+git://github.com/raphaa/django-urlshortener.git#egg=django-urlshortener

Configuration
=============

In settings.py::

  INSTALLED_APPS += ('urlshortener',)

  URLSHORTENER_SECRET = 'A password for creating a new short URL'

And in urls.py, add this line to the urlpatterns::

  url(r'^', include('urlshortener.urls')),

You can change the subfolder if you like.
