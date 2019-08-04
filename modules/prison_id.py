import sys
import utils
import helpers
from OinkModule import OinkModule
from collections import OrderedDict

# https://www.bop.gov/inmateloc

class Module(OinkModule):
    id_types = {
        'bop': None, 'dcdc': 'DCDC', 'fbi': 'FBI', 'ins':'INS'
    }

    DESCRIPTION="Search the Federal Bureau of Prisons inmate id."
    EXTENDED_DESCRIPTION = DESCRIPTION + "\n" + \
                "Returns max 100 results\n\n" + \
                "Usage = [id number] [type]\n" + \
                "Types = \n" + \
                    "\tbop\tBureau of Prisons number [default]\n" + \
                    "\tdcdc\tDCDC number (D.C. Department of Corrections)\n" + \
                    "\tfbi\tFBI number\n" + \
                    "\tins\tINS number\n"


    def __init__(self, state, query_args):
        OinkModule.__init__(self,
            state,
            "Prison ID",
            query_args,
            'post',
            'https://www.bop.gov/PublicInfo/execute/inmateloc',
            )

        search_type = None

        if (len(query_args) >= 2):
            if (query_args[1] in Module.id_types):
                # BOP is default, does not require inmateNumType
                if (Module.id_types[query_args[1]] != None):
                    search_type = self.id_types[query_args[1]]
            else:
                print(Module.id_types.keys())
                sys.exit("Unknown inmate ID type = {}".format(query_args[1]))

        self.data = {
            "todo": "query",
            "output": "json",
            "inmateNum": query_args[0].translate(None, '- '),
        }

        if (search_type): self.data['inmateNumType'] = search_type

        query_args

        self.run()

        ###############################################################
    def processResponse(self, response):
        json_response = response.json()
        if ('InmateLocator' not in json_response):
            sys.exit("Nonstandard response (bad input?)")

        if len(json_response['InmateLocator']) > 0:
            self.profile_data = []
            for inmate in json_response['InmateLocator']:

                entry = OrderedDict()
                entry["INMATE"] = "{} {}".format(inmate['inmateNum'],inmate['inmateNumType'])
                entry["First"] = inmate['nameFirst']
                entry["Last"] = inmate['nameLast']
                entry["Middle"] = inmate['nameMiddle']
                entry["Suffix"] = inmate['suffix']
                entry["Stats" ] = "{} {}, Age {}".format( inmate['race'], inmate['sex'], inmate['age'])
                entry["FACILITY"]="-----"
                entry["Facility Code"] = inmate['faclCode']
                entry["Facility Name"] = inmate['faclName']
                entry["Facility Type"] = inmate['faclType']
                entry["Facility URL"] = "https://www.bop.gov" + inmate['faclURL']
                entry["RELEASE"]="-----"
                entry["Proj Release"] =  inmate['projRelDate']
                entry["Actual Release"] =  inmate['actRelDate']
                entry["Release Code"] = inmate['releaseCode']

                self.profile_data.append(entry)
        else:
            print "No results"