from setuptools import setup, find_packages
import os

setup(
    name='django-urlshortener',
    version='0.1',
    description='A simple URL shortener for your Django project',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author='Raphael Jasjukaitis',
    author_email='webmaster@raphaa.de',
    url='http://github.com/raphaa/django-urlshortener/',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    install_requires=['Django'],
    include_package_data=True,
)
