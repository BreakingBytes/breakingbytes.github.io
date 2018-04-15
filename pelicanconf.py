#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mark Mikofski'
SITENAME = u'Breaking Bytes'
SITEURL = ''
SITELOGO = '/images/70s_Marko_Mustache_cropped.jpg'
FAVICON = '/images/breakingbytes.ico'
THEME = 'Flex'
PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
MAIN_MENU = True

# Blogroll
LINKS = (('poquito picante', 'https://poquitopicante.blogspot.com/'),
         ('bwanamarko', 'https://mikofski.github.io/'),
         ('old breaking bytes', 'https://breakingbytes.blogspot.com/'),)

# Social widget
SOCIAL = (('github', 'https://github.com/mikofski'),
          ('linkedin', 'https://www.linkedin.com/in/markmikofski/'),
          ('twitter', 'https://twitter.com/breaking_bytes'),
          ('google', 'https://plus.google.com/+MarkMikofski'),
          ('rss', 'feeds/all.atom.xml'))


MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2017

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
