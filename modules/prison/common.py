###############################################################
def printInmate(inmate):
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
