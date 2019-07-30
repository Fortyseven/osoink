import utils
import requests
from pprint import pprint

DESCRIPTION = "Search the Federal Bureau of Prisons inmate id."

EXTENDED_HELP = DESCRIPTION + "\n" + \
    "Returns max 100 results\n\n" + \
    "Usage: [id number] [type]\n" + \
    "Types: \n" + \
        "\tbop\tBureau of Prisons number [default]\n" + \
        "\tdcdc\tDCDC number (D.C. Department of Corrections)\n" + \
        "\tfbi\tFBI number\n" + \
        "\tins\tINS number\n"

POST_URL = "https://www.bop.gov/PublicInfo/execute/inmateloc"

id_types = ['bop', 'dcdc', 'fbi', 'ins']

# BOP? 10924-028

#curl "https://www.bop.gov/PublicInfo/execute/inmateloc" 
# -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0" 
# -H "Accept: application/json, text/javascript, */*; q=0.01" 
# -H "Accept-Language: en-US,en;q=0.5" --compressed 
# -H "Referer: https://www.bop.gov/inmateloc/" 
# -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" 
# -H "X-Requested-With: XMLHttpRequest" 
# -H "DNT: 1" 
# -H "Connection: keep-alive" 
# -H "Cookie: JSESSIONID=64BD6D809AC3D0C13C372CC5AA4A2AC5; AWSELB=DB516D6B02F3CFAC267AD082ED32FBEE93A5BE7283D2859BBA21D1F4C76146D2067C7F44CB2474D010F3B75FBC745EE822DEEF0146C68E811974794D00C6E21AE5344054934C4376B70DAE7C96E08420345C4673E4" 
# -H "Pragma: no-cache" -H "Cache-Control: no-cache" 
# --data "todo=query&output=json&inmateNum=&nameFirst=John&nameMiddle=&nameLast=Smith&race=&age=&sex="



def query(State, query_args):
    print "Searching for {}...".format(query_args[0])
    data = {
        "todo" : "query",
        "output" : "json",
        "inmateNum" : query_args[0].translate(None, '- '),
    }

    if (query_args[1]):
        if (query_args[1] == 'dcdc'):
            data['inmateNumType'] = "DCDC"

    response = requests.post(POST_URL, data)
    #data="nameFirst=John&nameMiddle=&nameLast=Smith&race=&age=&sex=")
    if (State.verbose):
        print "-------------"
        print "Raw response:"
        pprint(response.text)
        print response.status_code
    if (response.status_code == 200):
        dump_results(response)

def dump_results(response):
    json_response = response.json()
    if len(json_response['InmateLocator']) > 0:
        for inmate in json_response['InmateLocator']:
            print_inmate(inmate)
    else:
        print "No results"

def print_inmate(inmate):
    print "-------------"
    print "INMATE {} {}\n".format(inmate['inmateNum'],inmate['inmateNumType'])
    print "First:\t " + inmate['nameFirst']
    print "Last:\t " + inmate['nameLast']
    if (inmate['nameMiddle']):
        print "Middle:\t " + inmate['nameMiddle']
    if (inmate['suffix']):
        print "Suffix:\t " + inmate['suffix']

    print "{} {}, Age {}".format( inmate['race'], inmate['sex'], inmate['age'])
    print "\nFACILITY:\n"
    print "Facility Code:\t " + inmate['faclCode']
    print "Facility Name:\t " + inmate['faclName']
    print "Facility Type:\t " + inmate['faclType']
    print "Facility URL:\t " + "https://www.bop.gov" + inmate['faclURL']
    print "\nRELEASE:\n"
    if (inmate['projRelDate']):
        print "Proj Release:\t " + inmate['projRelDate']
    if (inmate['actRelDate']):
        print "Actual Release:\t " + inmate['actRelDate']
    if (inmate['releaseCode']):
        print "Release Code:\t " + inmate['releaseCode']
    
    

