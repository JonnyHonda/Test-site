#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'JonnyHonda'
SITENAME = u'Project K100'
SITESUBTITLE = 'My K100 ground up rebuild'
SITEIMAGE = '/Photos/Profile_Photos/20160820-192757-28491019084-o.jpg'
DESCRIPTION = 'I\'ve always loved the BMW K100 ever since I first aquired one back in the 1990s ' \
              'A beautiful massive K100LT. This is my Rebuild of the classic to pay homage to the marque.'

# SITEURL = 'http://test-site.sajb.co.uk'

THEME = "alchemy"

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'
DEFAULT_CATEGORY = 'Home'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = ARTICLE_URL
ARTICLE_LANG_URL = 'posts/{slug}-{lang}.html'
ARTICLE_LANG_SAVE_AS = ARTICLE_LANG_URL
STATIC_PATHS = ['Photos', ]

DELETE_OUTPUT_DIRECTORY = True
# OUTPUT_RETENTION = ["Photos",".jpeg",".jpg", ".JPG", "JPEG"]
# FILES_TO_COPY (('Photos'),('Photos'))
DISPLAY_PAGES_ON_MENU = True


# Blogroll
LINKS = (
    ('RealOEM', 'http://getpelican.com/'),
    ('MotorWorks', 'http://python.org/'),
    ('MotoBins', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'sitemap']
SITEMAP_SAVE_AS = 'sitemap.xml'