import string
from modules.social_networks import instagram
from modules.social_networks import gog

DESCRIPTION = "Finds references to a given username across various sites"

EXTENDED_HELP = DESCRIPTION + "\n" + \
    "Usage: [username]"


def query(state, args):
    username = string.lower(args[0].strip())

    instagram.scrapeUserInfo(state, username)
    gog.scrapeUserInfo(state, username)