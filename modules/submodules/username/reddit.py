import sys
import utils
import re
import json
import datetime
from pprint import pprint
from bs4 import BeautifulSoup
from ClusterProbe import ClusterProbe

class RedditProbe(ClusterProbe):
    def __init__(self, state, username):
        ClusterProbe.__init__(self,
            state,
            "Reddit",
            username,
            "get",
            "https://api.reddit.com/user/{}/about")
        self.custom_headers = {
            'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        self.run()

    def processResponse(self, response):
        res = response.json()
        self.profile_data['URL'] = self.url.format(self.username)
        self.profile_data['Name'] = res['data']['name']
        self.profile_data['Is Mod'] = res['data']['is_mod']
        self.profile_data['Is Employee'] = res['data']['is_employee']
        self.profile_data['Is Verified'] = res['data']['verified']
        self.profile_data['Created (UTC)'] = \
            datetime.datetime.utcfromtimestamp(res['data']['created'])
