import sys
import utils
import helpers
import re
import json
from pprint import pprint
from bs4 import BeautifulSoup

URL = "https://www.gog.com/u/{}"

class profile:
    username = None
    url = None
    title = None
    bio = {}


def scrapeUserInfo(state, username):
    profile.username = username
    helpers.StandardGET(state, URL.format(username), None, onSuccess, onFail)


def onFail(state, code, response):
    print "* Nothing on GOG..."


def onSuccess(state, response):
    html = response.text.encode('utf-8').strip()

    content = BeautifulSoup(response.text, 'html.parser')
    profile.title = content.title.contents[0]

    bio_start = html.index('window.profilesData.profileUser')
    bio_end = html.index('window.profilesData.serverNow')

    bio_text = html[bio_start:bio_end]

    regex = r"profileUser = (.*);"
    matches = re.search(regex, bio_text)
    bio_json_str = matches.group(1)

    bio_json = json.loads(bio_json_str)

    profile.bio['User ID'] = bio_json['userId']
    profile.bio['Created Date'] = bio_json['created_date']
    profile.bio['Achievements'] = bio_json['stats']['achievements']
    profile.bio['Games Owned'] = bio_json['stats']['games_owned']
    profile.bio['Hours Played'] = bio_json['stats']['hours_played']

    printProfile()


def printProfile():
    print "\n=== GOG ============================="
    if (profile.url):
        print "URL:\t\t{}".format(profile.url)
    else:
        print "URL:\t\t{}".format(URL.format(profile.username))

    print "Title:\t\t{}".format(profile.title)

    if (len(profile.bio) > 0):
        for value in profile.bio:
            print value + ":\t", profile.bio[value]

    print



