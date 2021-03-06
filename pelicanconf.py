#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Rituparna Panda'
SITENAME = u'Random Thoughts'
SITEURL = 'rituparnapanda.github.io'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('twitter-square', 'https://twitter.com/rituparna02'),
    ('linkedin', 'http://in.linkedin.com/in/rituparna02'),
    ('github', 'http://github.com/rituparnapanda'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['images']
COVER_IMG_URL = '/images/cover.jpg'
PROFILE_IMG_URL = '/images/profile.jpg'
THEME = 'pure-single'
READERS = {'html': None}
