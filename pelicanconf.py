#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'PyPGH'
SITENAME = 'PyPGH'
SITEURL = 'https://pypgh.netlify.com'

THEME = 'themes/pypgh'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Python on Reddit', 'https://www.reddit.com/r/Python/'),
    ('Python.org', 'http://python.org/'),
    ('Pittsburgh Python Developers', 'https://www.meetup.com/Python-Pittsburgh/'),
)

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

JS_FILE = 'main.js'

PLUGINS = ['pelican_webassets']
