#!/usr/bin/python

import os
import sys
import random
import time
import shutil
from optparse import OptionParser

usage = "usage: %prog -h to get help"

parser = OptionParser(usage)
parser.add_option("-i","--input",
                    action="store",
                    dest="inputdat",
                    type="string",
                    help="Choose file to import data",
                    metavar="FILE",
                    )

parser.add_option("-o","--output",
                    action="store",
                    dest="outputimage",
                    type="string",
                    help="write png image to FILE",
                    metavar="FILE",
                    default="confusion_matrix.png"
                    )

parser.add_option("-I","--INT",
                    action="store_true",
                    dest="intflag",
                    help="Choose using int or float",
                    default=False
                    )

(options, args) = parser.parse_args()  



# init 
CURRENT_DIR = os.getcwd()

def main():
    print("hello world!")


if __name__ == "__main__":
    print options
    main()
