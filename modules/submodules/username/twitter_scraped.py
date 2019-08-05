import sys
import utils
import re
import json
import dateutil.parser
from pprint import pprint
from bs4 import BeautifulSoup
from ClusterProbe import ClusterProbe

class TwitterScrapedProbe(ClusterProbe):
    def __init__(self, state, username):
        ClusterProbe.__init__(self,
            state,
            "Twitter",
            username,
            "get",
            "https://twitter.com/{}"
        )
        self.custom_headers = {
            'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }
        self.run()


    def processResponse(self, response):
        self.profile_data['URL'] = self.url.format(self.username)

        html = response.text.encode('utf-8').strip()

        content = BeautifulSoup(html, 'html.parser')
        self.profile_data['Title'] = (content.title.contents[0]).encode('utf-8').replace(' on Twitter', '').strip()

        metas = content.findAll("meta")

        for meta in metas:
            # pprint(meta)
            if meta.get("name") == "description":
                bio = meta.get("content").encode('utf-8')
                try:
                    skip_bio_start = bio.index( ').' ) + 2
                except:
                    skip_bio_start = 0
                finally:
                    self.profile_data['Bio'] = bio[skip_bio_start:].strip()