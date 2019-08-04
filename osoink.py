#!/usr/bin/python

import os
import sys
import re
import importlib
import argparse
import utils
from pprint import pprint
from bs4 import BeautifulSoup

modules = {}

class State:
    verbose = False
    random_user_agent = False
    utils = utils


def load_modules():
    pysearchre = re.compile('.py$', re.IGNORECASE)
    plugin_files = filter(pysearchre.search, os.listdir(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'modules')))

    for plugin_name in plugin_files:
        shortname = os.path.splitext(plugin_name)[0]
        if shortname == '__init__':
            continue
        modules[shortname] = importlib.import_module('modules.' + shortname).Module

    return modules

def list_modules():
    print("Modules available: (use --module to specify)")
    print("----------------------")
    for module_name in modules:
        print("{}\t{}".format(module_name, modules[module_name].DESCRIPTION))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', action="store_true", help="verbose")
    parser.add_argument('--list-modules', action="store_true", help="list available modules")
    parser.add_argument('--random-user-agent', action="store_true", default=False, help="use a random user agent")
    parser.add_argument('module', type=str, action="store", help="Query using module name", nargs='?')
    parser.add_argument('query', type=str, action="store", help="Search query", nargs=argparse.REMAINDER)
    args  = parser.parse_args()

    modules = load_modules()

    if (args.v):
        print(args)
        print

    if (args.list_modules):
        list_modules()
        sys.exit(1)

    if (args.module == None):
        parser.error("A module name is required with --module")
        sys.exit(1)

    if (args.query == None):
        print(modules[args.module].EXTENDED_HELP)
        sys.exit(1)

    State.verbose = args.v
    State.random_user_agent = args.random_user_agent

    # Call the module with the query
    modules[args.module](State, args.query)

if __name__ == "__main__":
    main()