# -*- coding: utf-8 -*-
#quckstarted Options:
#
# sqlalchemy: True
# auth:       sqlalchemy
# mako:       True
#
#

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys, os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

README = README.split(".. split here")[1]

setup(
    name='narcissus',
    version='0.3',
    description='',
    author='Ralph Bean',
    author_email='rbean@redhat.com',
    #url='',
    install_requires=[
        "TurboGears2 >= 2.1",
        "Mako",
        "zope.sqlalchemy >= 0.4",
        "repoze.tm2 >= 1.0a5",
        "repoze.what-quickstart",
        "repoze.what >= 1.0.8",
        "repoze.what-quickstart",
        "repoze.who-friendlyform >= 1.0.4",
        "repoze.what-pylons >= 1.0",
        "repoze.what.plugins.sql",
        "repoze.who == 1.0.18",
        "Moksha",
        "sqlalchemy",
        "virtualenvcontext",
        "pymysql_sa",
        "MySQL-python",
        "decorator",
        "geojson",
        "pygeoip",
        "ansi2html",
        "tw2.polymaps>=0.1a3",
        "tw2.jqplugins.jqplot",
        "tw2.slideymenu>=2.0b1",
        "tw2.rrd>=2.0b13",
        "tw2.jit>=0.3.0",
        "pylons==1.0", # For TG2 madness
        "webob==1.8.8", # For TG2 madness
        ],
    setup_requires=["PasteScript >= 1.7"],
    paster_plugins=['PasteScript', 'Pylons', 'TurboGears2'],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['WebTest >= 1.2.3',
                   'nosetests',
                   'coverage',
                   'wsgiref'
                   'repoze.who-testutil >= 1.0.1',
                   ],
    package_data={'narcissus': ['i18n/*/LC_MESSAGES/*.mo',
                                 'templates/*/*',
                                 'public/*/*']},
    message_extractors={'narcissus': [
            ('**.py', 'python', None),
            ('templates/**.mako', 'mako', None),
            ('public/**', 'ignore', None)]},
    entry_points={
        'paste.app_factory': (
            'main = narcissus.config.middleware:make_app',
        ),
        'paste.app_install': (
            'main = pylons.util:PylonsInstaller',
        ),
        'moksha.stream' : (
            'series_pro = narcissus.consumers:TimeSeriesProducer',
            'random_lol = narcissus.producers:RandomIPProducer',
        ),
        'moksha.consumer': (
            'raw_ip = narcissus.consumers:RawIPConsumer',
            'httpdlight = narcissus.consumers:HttpLightConsumer',
            'latlon2geo = narcissus.consumers:LatLon2GeoJsonConsumer',
            'series_con = narcissus.consumers:TimeSeriesConsumer',
        ),
        'moksha.widget': (
            'narc_map = narcissus.widgets:NarcissusMapWidget',
            'narc_graph = narcissus.widgets:NarcissusGraphWidget',
            'narc_plot = narcissus.widgets:NarcissusPlotWidget',
        ),
    },
)
