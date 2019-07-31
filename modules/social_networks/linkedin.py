import sys
import utils
import helpers
import re
from pprint import pprint
from bs4 import BeautifulSoup

URL = "https://www.linkedin.com/in/{}/"

class li_profile:
    username = None
    # url = None
    # title = None
    # desc = None
    # bio = None


def scrapeUserInfo(state, username):
    ig_profile.username = username
    helpers.StandardGET(state, URL.format(username), None, onSuccess, onFail)


def onFail(state, code, response):
    print "* Nothing on LinkedIn..."


def onSuccess(state, response):
    html = response.text.encode('utf-8').strip()

    regex = r"\"biography\":\"([^\"]*)\""
    matches = re.search(regex, html)
    ig_profile.bio = matches.group(1)

    content = BeautifulSoup(response.text, 'html.parser')
    ig_profile.title = content.findAll("meta", property="og:title")[0]['content'].encode('utf-8')
    ig_profile.title = ig_profile.title[:-31].strip()
    ig_profile.desc = content.findAll("meta", property="og:description")[0]['content'].encode('utf-8')
    ig_profile.desc = ig_profile.desc[:-70].strip()
    ig_profile.url = content.findAll("meta", property="og:url")[0]['content'].encode('utf-8')

    printProfile()


def printProfile():
    print "\n=== INSTAGRAM ============================="
    if (ig_profile.url):
        print "URL:\t{}".format(ig_profile.url)
    else:
        print "URL:\t{}".format(URL.format(ig_profile.username))
        print "Private account?"
    if (ig_profile.title):
        print "Title:\t{}".format(ig_profile.title)
    if (ig_profile.desc):
        print "Desc:\t{}".format(ig_profile.desc)
    if (ig_profile.bio):
        print "Bio:\t{}".format(ig_profile.bio)


