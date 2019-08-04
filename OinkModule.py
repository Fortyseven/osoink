import sys
import string
import helpers
import math
from collections import OrderedDict

class OinkModule:
    DESCRIPTION = None
    EXTENDED_DESCRIPTION = None
    def __init__(self, state, module_name, query_args, method=None, url=None):
        self.module_name = module_name
        self.state = state
        self.profile_data = OrderedDict()
        self.custom_headers = {}
        self.data = {}
        self.query_args = query_args
        self.method = method
        self.url = url

        if (len(query_args) == 0):
            sys.exit(self.EXTENDED_DESCRIPTION)


    def processResponse(self, response):
        raise NotImplementedError


    def onSuccess(self, response):
        self.processResponse(response)
        self.showReport()


    def onFail(self, response):
        print "* Nothing on {} ({}) ".format(self.module_name, response.status_code)


    def run(self):
        if self.method == 'get':
            helpers.StandardGET(self.state,
                self.url,
                self.data,
                self.onSuccess,
                self.onFail,
                self.custom_headers)
        elif self.method == 'post':
            helpers.StandardPOST(self.state,
                self.url,
                self.data,
                self.onSuccess,
                self.onFail,
                self.custom_headers)
        elif self.method == None:
            self.onSuccess(None)
        else:
            raise Exception("Illegal or unspecified method for run() specified in " + self.module_name)


    def showReport(self):
        # print "### {} #########################".format(string.upper(self.module_name))
        # max_tab_width = 0

        # for key in self.profile_data.keys():
        #     if (len(key) > max_tab_width):
        #         max_tab_width = len(key)

        # print math.ceil(max_tab_width/4)

        if (type(self.profile_data) == list):
            for entry in self.profile_data:
                self.processEntry(entry)
        else:
            self.processEntry(self.profile_data)


    def processEntry(self, single_entry):
        for data in single_entry:
            val = single_entry[data]
            val_type = type(single_entry[data])
            if (val_type == str):
                try:
                    val = val.encode('utf-8')
                except:
                    pass
            elif (val_type == int):
                val = format(val, ",")

            # FIXME - make this a bit smarter later
            tabsize=2
            if (len(data) <= 4): tabsize=3

            print "- {}:{}{}".format(data,"\t"*tabsize ,val)
        print
