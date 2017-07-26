# -*- coding:utf-8 -*-

import os
import argparse
import re

parser = argparse.ArgumentParser(description='look for _(" pattern in all .py file')
parser.add_argument('--ifile', '-i', dest='ifile', type=str, help='The input file or directories, default is ./',
                    default='./')
parser.add_argument('--ofile', '-o', dest='ofile', type=str,
                    help='The file to store the results, default is ./keywordlookup_output',
                    default='./keywordlookup_output')
args = parser.parse_args()


def keywordlookup():
    find = re.compile(r'_\(["\']')
    ext = re.compile(r'\.py$')
    n = 0

    with open(args.ofile, "w") as out:
        if os.path.isdir(args.ifile):
            dirs = os.listdir(args.ifile)
            for file in dirs:
                if not os.path.isdir(file) and re.search(ext, file):
                    with open(args.ifile + '/' + file, "r") as f:
                        for line in f:
                            n += 1
                            if re.search(find, line):
                                out.write(os.path.abspath(args.ifile + '/' + file) + ':\t' + 'line:' + str(n) + '\n')
                                out.write(line + '\n')
        else:
            if re.search(ext, args.ifile):
                with open(args.ifile, "r") as f:
                    for line in f:
                        n += 1
                        if re.search(find, line):
                            out.write(os.path.abspath(args.ifile) + ':\t' + 'line:' + str(n) + '\n')
                            out.write(line + '\n')


if __name__ == '__main__':
    keywordlookup()
