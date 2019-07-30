import os
import random

def random_line(filename):
    f = open(filename, "r")
    line = next(f)
    for num, aline in enumerate(f, 2):
        if random.randrange(num): continue
        line = aline
    f.close()
    return line.strip()

def getRandomUserAgent():
    return random_line(os.path.dirname(os.path.realpath(__file__))+\
                        "/data/user-agents.txt")

