# -*- coding:utf-8 -*-

import os
import argparse
import re


def recompile():
    s1 = re.compile(r'^\d$')
    s2 = re.compile(r'^\d\d$')
    s3 = re.compile(r'^\d\d\d$')
    s4 = re.compile(r'^\d\d\d\d$')
    s5 = re.compile(r'^\d\d\d\d\d$')
    s6 = re.compile(r'^\d\d\d\d\d·\d\d\d-·\d\d\d$')
    s7 = re.compile(r'^\d\d\d\d\d·\d\d\d$')
    return s1, s2, s3, s4, s5, s6, s7


def cutstring(string, s1, s2, s3, s4, s5, s6, s7):
    ret = 0
    parent = ""
    if s1.search(string):
        ret = 1
        parent = "-1"
    if s2.search(string):
        ret = 2
        parent = string[0:1]
    if s3.search(string):
        ret = 3
        parent = string[0:2]
    if s4.search(string):
        ret = 4
        parent = string[0:3]
    if s5.search(string):
        ret = 5
        parent = string[0:4]
    if s6.search(string):
        ret = 6
        parent = string[0:5]
    if s7.search(string):
        ret = 7
        parent = string[0:5]
    return parent, ret


def parentid(ifile, ofile):
    s1, s2, s3, s4, s5, s6, s7 = recompile()
    parentstore = ""

    ifile = os.path.expanduser(os.path.expandvars(ifile))
    ofile = os.path.expanduser(os.path.expandvars(ofile))

    with open(ofile, "w") as of:
        with open(ifile, "r") as f:
            for line in f:
                parent, ret = cutstring(line, s1, s2, s3, s4, s5, s6, s7)
                if ret == 0:
                    of.write("\n")
                if ret > 0 and ret < 7:
                    of.write("\t" + parent + "\n")
                    if ret == 6:
                        parentstore = line[0:16]
                if ret == 7:
                    if parentstore is not "":
                        of.write("\t" + parentstore + "\n")
                        parentstore = ""
                    else:
                        of.write("\t" + parent + "\n")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='look for pattern in files')
    parser.add_argument('--ifile', '-i', dest='ifile', type=str, help='The input file or directories, default is ./',
                        default='./')
    parser.add_argument('--ofile', '-o', dest='ofile', type=str,
                        help='The file to store the results, default is ./keywordlookup_output',
                        default='./keywordlookup_output')
    args = parser.parse_args()

    parentid(args.ifile, args.ofile)
