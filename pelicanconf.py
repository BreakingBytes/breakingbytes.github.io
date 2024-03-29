#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Mark Mikofski'
SITENAME = u'Breaking Bytes'
SITESUBTITLE = 'My personal blog about <a rel="me" href="https://fosstodon.org/@mikofski">me</a>'
SITEURL = ''
SITELOGO = '/images/70s_Marko_Mustache_cropped.jpg'
FAVICON = '/images/breakingbytes.ico'
THEME = '../pelican-themes/Flex'
PATH = 'content'
STATIC_PATHS = ['images']

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
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
          ('mastodon', 'https://fosstodon.org/@mikofski'),
          ("stack-overflow", "https://stackoverflow.com/users/1020470/mark-mikofski"),
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

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

GOOGLE_GLOBAL_SITE_TAG = 'G-XB3X8X7LK5' # Your Google Analytics 4 Property ID
