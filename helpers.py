import requests
import sys
import utils
from pprint import pprint

###############################################################
def StandardPOST(state, url, data, success_func, fail_func = None):
    try:
        headers = {}

        if (state.random_user_agent):
            if (state.verbose): print("Using random agent")
            headers['User-Agent'] = utils.getRandomUserAgent()
            
        response = requests.post(url, data, headers=headers)        
    except requests.exceptions.ConnectionError as err:
        sys.exit(err)   
    
    if (state.verbose):
        print "#####################"
        print "Request URL:"
        pprint(url)
        print "\nRequest data:"
        pprint(data)
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
