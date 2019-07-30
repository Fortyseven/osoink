import sys
import utils
import helpers
from modules.prison.common import printInmate

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

id_types = {
    'bop': None, 'dcdc': 'DCDC', 'fbi': 'FBI', 'ins':'INS'
}

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

###############################################################
def query(state, query_args):
    data = {
        "todo" : "query",
        "output" : "json",
        "inmateNum" : query_args[0].translate(None, '- '),
    }

    if (query_args[1]):
        if (query_args[1] in id_types):
            # BOP is default, does not require inmateNumType
            if (id_types[query_args[1]] != None):
                data['inmateNumType'] = id_types[query_args[1]]
        else:
            print(id_types.keys())
            sys.exit("Unknown inmate ID type: {}".format(query_args[1]))
        
    print "Searching for {}...".format(query_args[0])

    helpers.StandardPOST(state, POST_URL, data, onSuccess)

    #data="nameFirst=John&nameMiddle=&nameLast=Smith&race=&age=&sex="
    
    

###############################################################
def onSuccess(state, response):
    json_response = response.json()
    if ('InmateLocator' not in json_response):
        sys.exit("Nonstandard response (bad input?)")

    if len(json_response['InmateLocator']) > 0:
        for inmate in json_response['InmateLocator']:
            printInmate(inmate)
    else:
        print "No results"