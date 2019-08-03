import sys
import utils
import helpers
import re
import json
from pprint import pprint

# FIXME - This module is currently incomplete, requiring incorporation of an API key. We'll also
# need to add a config file for holding this kind of data. No doubt it will be used elsewhere by
# other modules.

URL = "https://api.twitter.com/graphql/SEn6Mq-OakvVOT1CJqUO2A/UserByScreenName?variables=%7B%22screen_name%22%3A%22{}%22%2C%22withHighlightedLabel%22%3Atrue%7D"

def scrapeUserInfo(state, username):
    helpers.StandardGET(state, URL.format(username),
        None, onSuccess, onFail,
        {
            'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
            'Accept'    : '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
            'Referer': 'https://mobile.twitter.com/',
            'content-type': 'application/json',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-guest-token': '1157226596543213568',
            'x-twitter-client-language': 'en',
            'x-twitter-active-user': 'yes',
            'x-csrf-token': '8d84dff09f61b547e199de05a96127d6',
            'Origin': 'https://mobile.twitter.com',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Cookie': '_twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCEAhpktsAToMY3NyZl9p%250AZCIlYjliNjcwMzNkYmVkNmExOTAxMzg5ZTg4NDY2YWZmMGU6B2lkIiUwMTk2%250AOGIyYTk0NzcxYjhmN2QyYTUzNDBkZDgyNWU4ZA%253D%253D--8e1de78b6203cf69362a8d2dd2afe03d6b0ec27e; personalization_id=v1_KT1I6w8LbmUyBETBq0+pBw==; guest_id=v1%3A156463727442936063; rweb_optin=side_no_out; ct0=8d84dff09f61b547e199de05a96127d6; gt=1157226596543213568',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers'
        }
    )


def onFail(state, code, response):
    print "* Nothing on Twitter ({})...".format(code)


def onSuccess(state, response):
    printProfile(response.json()['data']['user'])


def printProfile(response):
    print "\n=== TWITTER ============================="
    if (response['legacy']):
        legacy = response['legacy']

        verified = ""
        if (legacy['verified']): verified = "[VERIFIED]"

        print "* Name:\t\t{} (@{}) {}".format(legacy['name'].encode('utf-8'), legacy['screen_name'], verified)
        print "* Created:\t", legacy['created_at']
        print "* Bio:\t\t\"{}\"".format(legacy['description'].encode('utf-8'))

        if (legacy['location']):
            print "* Location:\t", legacy['location']

        if (response['legacy_extended_profile']):
            extended = response['legacy_extended_profile'];
            print "* Birthdate:\t", "{}/{} ({})".format(extended['birthdate']['month'], extended['birthdate']['day'], extended['birthdate']['visibility'])

        print "* Total Tweets:\t", format(legacy['statuses_count'], ',')
        print "* Followers:\t", format(legacy['followers_count'], ',')
        print "* Friends:\t", format(legacy['friends_count'], ',')
        print "* Favorites:\t", format(legacy['favourites_count'], ',')
        print "* Listed:\t", format(legacy['listed_count'], ',')
        print "* Media count:\t", format(legacy['media_count'], ',')

        print "* Advertiser Account Type:", legacy['advertiser_account_type']
    print



