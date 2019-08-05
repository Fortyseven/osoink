import sys
import utils
import helpers
import string
from ClusterModule import ClusterModule
from collections import OrderedDict

from submodules.username.twitter_scraped import TwitterScrapedProbe
from submodules.username.gog import GOGProbe
from submodules.username.instagram import InstagramProbe
from submodules.username.reddit import RedditProbe

class Module(ClusterModule):
    DESCRIPTION = "Finds references to a given username across various sites"
    EXTENDED_DESCRIPTION = DESCRIPTION + "\n" + \
                "Usage: [username]"


    def __init__(self, state, query_args):
        ClusterModule.__init__(self,
            state,
            "Username",
            query_args
            )


    def processResponse(self, response):
        username = string.lower(self.query_args[0].strip())

        # Major social media
        TwitterScrapedProbe(self.state, username)
        InstagramProbe(self.state, username)
        RedditProbe(self.state, username)

        # Gaming
        GOGProbe(self.state, username)
