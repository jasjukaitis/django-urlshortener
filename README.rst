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

And in urls.py, add this line to the urlpatterns::

  url(r'^(?P<shortid>\S+)/$', 'urlshortener.views.open_shortid'),

You can change the subfolder if you like.
