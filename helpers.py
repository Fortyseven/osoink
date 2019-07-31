import requests
import sys
import utils
from pprint import pprint

###############################################################
def StandardPOST(state, url, data, success_func, fail_func = None):
    headers = {}
    response = None

    if (state.random_user_agent):
        if (state.verbose): print("* Using random agent")
        headers['User-Agent'] = utils.getRandomUserAgent()

    try:
        response = requests.post(url, data, headers=headers, timeout=5)
    except requests.exceptions.ConnectionError as err:
        sys.exit(err)
    finally:
        if (state.verbose):
            print "\n#####################"
            if (state.random_user_agent):
                print("* Using random agent")
            print "* Request URL:" + url
            print "\nRequest data:"
            pprint(data)
            if (response):
                print "\nResponse code:\t{}".format(response.status_code)
                print "\nResponse text:"
                pprint(response.text)

            print "\n#####################\n"

    if (response.status_code == 200):
        success_func(state, response)
    else:
        if (callable(fail_func)):
            fail_func(state, response.status_code, response)
            sys.exit(1)
        else:
            print "## ERR: Received {} on POST request".format(response.status_code)
            sys.exit(1)

###############################################################
def StandardGET(state, url, data, success_func, fail_func=None):
    headers = {}
    response = None

    if (state.random_user_agent):
        if (state.verbose): print("* Using random agent")
        headers['User-Agent'] = utils.getRandomUserAgent()

    try:
        response = requests.get(url, data, headers=headers, timeout=5)
    except requests.exceptions.ConnectionError as err:
        sys.exit(err)
    finally:
        if (state.verbose):
            print "\n#####################"
            if (state.random_user_agent):
                print("* Using random agent")
            print "* Request GET URL:" + url
            print "\nRequest data:"
            pprint(data)
            if (response):
                print "\nResponse code:\t{}".format(response.status_code)
                print "\nResponse text:"
                pprint(response.text)

            print "\n#####################\n"

    if (response.status_code == 200):
        success_func(state, response)
    else:
        if (callable(fail_func)):
            fail_func(state, response.status_code, response)
            sys.exit(1)
        else:
            print "## ERR: Received {} on GET request".format(response.status_code)
            sys.exit(1)
