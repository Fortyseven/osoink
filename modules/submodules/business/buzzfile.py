import sys
import utils
import re
import json
import datetime
from pprint import pprint
from bs4 import BeautifulSoup
from ClusterProbe import ClusterProbe
from collections import OrderedDict


class BuzzfileProbe(ClusterProbe):
    def __init__(self, state, query):
        ClusterProbe.__init__(self,
            state,
            "Buzzfile",
            "post",
            "http://www.buzzfile.com/Search/Company/QuickSearch")

        self.data = {
            'term': query,
            'stype' : '1',
            'optional' : ''
        }
        self.custom_headers = {
            'Host': 'www.buzzfile.com',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Referer': 'http://www.buzzfile.com/business/Necs-475-221-8200',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'X-Requested-With': 'XMLHttpRequest',
            'DNT': '1',
            'Alt-Used': 'www.buzzfile.com:443',
            'Connection': 'keep-alive',
            'Cookie': '__cfduid=dbea9e109f2b405cfabbfcc3aaf02df771564907066; ASP.NET_SessionId=zy35eyil0bj5na1ykjcycc1h; __cfduid=dbea9e109f2b405cfabbfcc3aaf02df771564907066; ASP.NET_SessionId=zy35eyil0bj5na1ykjcycc1h',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'TE': 'Trailers'
        }
        self.run()


    def processResponse(self, response):
        self.profile_data = []

        for entry in response.json():
            row = OrderedDict()
            row["Name"] = entry['Name']
            row["Location"] = "{}, {}".format(entry["City"], entry['State'])
            row["PhoneNumber"] = entry['PhoneNumber']
            row["TradeStyle"] = entry['TradeStyle']
            row["URL"] = "http://www.buzzfile.com/business/{}".format(entry["Slang"])
            #row["IsDeleted"] = entry["IsDeleted"],
            #row["Employee"] = entry["Employee"],
            row["Id"] = str(entry['Id'])

            self.profile_data.append(row)

