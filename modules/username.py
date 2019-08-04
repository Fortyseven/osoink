import sys
import utils
import helpers
import string
from OinkModule import OinkModule
from collections import OrderedDict

from modules.social_networks.twitter_scraped import TwitterScrapedProbe
from modules.social_networks.gog import GOGProbe
from modules.social_networks.instagram import InstagramProbe
from modules.social_networks.reddit import RedditProbe

class Module(OinkModule):
    DESCRIPTION = "Finds references to a given username across various sites"
    EXTENDED_DESCRIPTION = DESCRIPTION + "\n" + \
                "Usage: [username]"


    def __init__(self, state, query_args):
        # This reduced init lets us use processResponse as a virtual 'main'
        # to run the subqueries
        OinkModule.__init__(self,
            state,
            "Username",
            query_args
            )

        self.run()

        ###############################################################
    def processResponse(self, response):
        username = string.lower(self.query_args[0].strip())

        # Major social media
        TwitterScrapedProbe(self.state, username)
        InstagramProbe(self.state, username)
        RedditProbe(self.state, username)

        # Gaming
        GOGProbe(self.state, username)
