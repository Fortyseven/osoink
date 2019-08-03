import string

from modules.social_networks.twitter_scraped import TwitterScrapedProbe
from modules.social_networks.gog import GOGProbe
from modules.social_networks.instagram import InstagramProbe
from modules.social_networks.reddit import RedditProbe

DESCRIPTION = "Finds references to a given username across various sites"

EXTENDED_HELP = DESCRIPTION + "\n" + \
    "Usage: [username]"



def query(state, args):
    username = string.lower(args[0].strip())

    # Major social media
    TwitterScrapedProbe(state, username)
    InstagramProbe(state, username)
    RedditProbe(state, username)

    # Gaming
    GOGProbe(state, username)
