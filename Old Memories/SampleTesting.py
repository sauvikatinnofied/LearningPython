__author__ = 'Sauvik'
import sys
#################################################
#   DEFINING THE MAIN FUNCTION OF THE MODULE
################################################

def main(startIndex, endIndex):
    for x in range(startIndex, endIndex):
        print ('Loop iteration with ', x )
    # Out of the for loop
    print ('Welcome back to your world Mr. ', sys.argv[0])

## Going to execute the main function if this file is going to be executed from command line

if __name__ == '__main__':
    main(0,10)