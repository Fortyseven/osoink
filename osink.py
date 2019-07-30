#!/usr/bin/python

import os
import sys
import re
import importlib
import argparse
import utils
from bs4 import BeautifulSoup

modules = {}

class State:
    verbose = False
    utils = utils


def load_modules():
    pysearchre = re.compile('.py$', re.IGNORECASE)
    plugin_files = filter(pysearchre.search, os.listdir(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'modules')))
    
    for plugin_name in plugin_files:
        shortname = os.path.splitext(plugin_name)[0]
        if shortname == '__init__':
            continue
        modules[shortname] = importlib.import_module('modules.' + shortname)

    return modules

def list_modules():
    print("Modules available: (use --module to specify)")
    print("----------------------")
    for module_name in modules:
        print("{}\t{}".format(module_name, modules[module_name].DESCRIPTION))

def main():    
    parser = argparse.ArgumentParser("osink - osint search tool")
    parser.add_argument('-v', action="store_true", help="verbose")
    parser.add_argument('--list-modules', action="store_true", help="list available modules")
    parser.add_argument('module', type=str, action="store", help="Query using module name")
    parser.add_argument('query', type=str, action="store", help="Search query", nargs='?')
    parser.add_argument('arg1', type=str, action="store", help="Optional argument 1", nargs='?')
    parser.add_argument('arg2', type=str, action="store", help="Optional argument 2", nargs='?')
    args  = parser.parse_args()

    if (args.list_modules): 
        list_modules()
        sys.exit(1)

    if (args.module == None):
        parser.error("A module name is required with --module")    
        sys.exit(1)

    modules = load_modules()

    if (args.query == None):
        print(modules[args.module].EXTENDED_HELP)
        sys.exit(1)

    State.verbose = args.v

    # Call the module with the query
    modules[args.module].query(State,[args.query, args.arg1, args.arg2])

if __name__ == "__main__":
    main()