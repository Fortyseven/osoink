import sys
import string
import helpers
import math
from OinkModule import OinkModule
from collections import OrderedDict

class ClusterModule(OinkModule):
    def __init__(self, state, module_name, query_args):
        # This reduced init lets us use processResponse as a virtual 'main'
        # to run the subqueries
        OinkModule.__init__(self,
            state,
            module_name,
            query_args
            )

        self.run()

