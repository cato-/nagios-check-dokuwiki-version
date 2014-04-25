#!/usr/bin/env python

import sys

import dokuwikixmlrpc
import requests

import settings

dw = dokuwikixmlrpc.DokuWikiClient("https://%s/" % settings.wiki, settings.user, settings.passwd)

current_version =  dw.dokuwiki_version.split(" ")[1]

upstream_version_url = "https://raw.githubusercontent.com/splitbrain/dokuwiki/stable/VERSION"

upstream_version = requests.get(upstream_version_url).text.strip()
upstream_version_split = upstream_version.split(" ")[0]


if current_version == upstream_version_split:
    print "OK - version %s" % upstream_version
    sys.exit(0)
else:
    print "CRITICAL - new upstream version %s" % upstream_version
    sys.exit(2)
