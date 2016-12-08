import sys
import multiprocessing
from optparse import OptionParser
from crackmethods import Dictionary


def Main(options):
    options.zipfile = sys.argv[1]
    if options.cores is None:
        options.cores = multiprocessing.cpu_count() - 2
        # If -c/--cores option is not set,
        # use two less cores than the total cores that
        # the user has.
        # @TODO: If multiprocessing.cpu_count() < 3, set
        # options.cores to 2.
    else:
        print(options.cores)

    # Check if dictionary file is valid,
    # otherwise load default one
    if options.dictfile is None:
        options.dictfile = "default.txt"
        print("Default dictionary loaded")
    else:
        try:
            with open(options.dictfile) as f:
                print("Loaded dict successfully")
        except:
            options.dictfile = "defaults.txt"
            print("Bad dictionary file, loaded default")

    # Last step after sorting through options,
    # launch actual attacks
    if options.brute is None:
        # Begin dictionary attack
        print("Dictionary attack started")
        Dictionary.InitAttack(options)
    else:
        # Begin brute force attack
        print("Brute force attack started")


if __name__ == '__main__':
    usage = "usage: %prog [options] <zip file>"
    parser = OptionParser(usage=usage)
    parser.add_option("-d", "--dict", dest="dictfile",
                      help="Pick your dictionary file")
    parser.add_option("-b", "--brute", action="store_false", dest="brute",
                      help="Opt to brute force the zip")
    parser.add_option("-c", "--cores", dest="cores",
                      help="Number of cores to use in cracking")
    parser.add_option("-q", "--quiet", action="store_false",
                      dest="verbose", default=True,
                      help="Whether or not to surpress verbose output")

    (options, args) = parser.parse_args()
    Main(options)
