import sys
import utils
import re
import json
import dateutil.parser
from pprint import pprint
from bs4 import BeautifulSoup
from ClusterProbe import ClusterProbe

class GOGProbe(ClusterProbe):
    def __init__(self, state, username):
        ClusterProbe.__init__(self,
            state,
            "GOG",
            username,
            "get",
            "https://www.gog.com/u/{}")
        self.run()

    def processResponse(self, response):
        self.profile_data['URL'] = self.url.format(self.username)

        html = response.text.encode('utf-8').strip()

        content = BeautifulSoup(response.text, 'html.parser')
        self.profile_data['Title'] = content.title.contents[0]

        ## -----

        bio_start = html.index('window.profilesData.profileUser')
        bio_end = html.index('window.profilesData.serverNow')

        bio_text = html[bio_start:bio_end]

        regex = r"profileUser = (.*);"
        matches = re.search(regex, bio_text)
        bio_json_str = matches.group(1)

        bio_json = json.loads(bio_json_str)

        self.profile_data['User ID'] = bio_json['userId']
        self.profile_data['Created Date'] = \
            dateutil.parser.parse(bio_json['created_date']).strftime("%Y-%m-%d @ %I:%M:%S%p")
        self.profile_data['Achievements'] = bio_json['stats']['achievements']
        self.profile_data['Games Owned'] = bio_json['stats']['games_owned']
        self.profile_data['Hours Played'] = bio_json['stats']['hours_played']
