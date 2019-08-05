import sys
import utils
import helpers
import string
from ClusterModule import ClusterModule
from collections import OrderedDict

# from modules.social_networks.twitter_scraped import TwitterScrapedProbe
# from modules.social_networks.gog import GOGProbe
# from modules.social_networks.instagram import InstagramProbe
# from modules.social_networks.reddit import RedditProbe

class Module(ClusterModule):
    DESCRIPTION = "Finds references to a given business name across various sites"
    EXTENDED_DESCRIPTION = DESCRIPTION + "\n" + \
                "Usage: [query]\n"\
                "Use quotes for multiple words."


    def __init__(self, state, query_args):
        ClusterModule.__init__(self,
            state,
            "Business",
            query_args
            )


    def processResponse(self, response):
        query = string.lower(self.query_args[0].strip())

        # Major social media
        # TwitterScrapedProbe(self.state, query)
        # InstagramProbe(self.state, query)
        # RedditProbe(self.state, query)

        # # Gaming
        # GOGProbe(self.state, query)
