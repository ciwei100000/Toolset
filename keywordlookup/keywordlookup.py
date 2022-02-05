# -*- coding:utf-8 -*-

import os
import argparse
import re


def keywordlookup(ifile, ofile, fi, fe, pattern, pe):

    ifile = os.path.expanduser(os.path.expandvars(ifile))
    ofile = os.path.expanduser(os.path.expandvars(ofile))

    find = re.compile(r'%s' % pattern)
    fi_n = 0
    fe_n = 0
    pe_n = 0

    if fi != '':
        ext_i = re.compile(r'%s' % fi)
        fi_n = 1

    if fe != '':
        ext_e = re.compile(r'%s' % fe)
        fe_n = 1

    if pe != '':
        ext_pe = re.compile(r'%s' % pe)
        pe_n = 1

    with open(ofile, "w") as out:
        if os.path.isdir(ifile):
            for dirpath, dirnames, filenames in os.walk(ifile):
                for filename in filenames:
                    do = 0
                    if fi_n:
                        if re.search(ext_i, filename):
                            do = 1
                    else:
                        do = 1
                    if fe_n:
                        if re.search(ext_e, filename):
                            do = 0
                    if do:
                        filepath = os.path.join(dirpath, filename)
                        if pe_n:
                            if re.search(ext_pe, filepath):
                                do = 0
                    if do:
                        with open(filepath, "r") as f:
                            n = 0
                            for line in f:
                                n += 1
                                if re.search(find, line):
                                    out.write(filepath + ':\t' +
                                              'line:' + str(n) + '\n')
                                    out.write(line + '\n')
        else:
            do = 0
            if fi_n:
                if re.search(ext_i, ifile):
                    do = 1
            else:
                do = 1
            if fe_n:
                if re.search(ext_e, ifile):
                    do = 0
            if do:
                with open(ifile, "r") as f:
                    n = 0
                    for line in f:
                        n += 1
                        if re.search(find, line):
                            #out.write(os.path.abspath(ifile) + ':\t' + 'line:' + str(n) + '\n')
                            out.write(line + '\n')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='look for pattern in files')
    parser.add_argument('--ifile', '-i', dest='ifile', type=str, help='The input file or directories, default is ./',
                        default='./')
    parser.add_argument('--ofile', '-o', dest='ofile', type=str,
                        help='The file to store the results, default is ./keywordlookup_output',
                        default='./keywordlookup_output')
    parser.add_argument('--file_include_rule', '-fi', dest='fi', type=str,
                        help='Use regular expression to include input filenames', default='')
    parser.add_argument('--file_exclude_rule', '-fe', dest='fe', type=str,
                        help='Use regular expression to exclude input filenames', default='')
    parser.add_argument('--pattern', '-p', dest='pattern', type=str,
                        help='Use regular expression to define the pattern to look for', default='_\(["\']')
    parser.add_argument('--path_exclude_rule', '-pe', dest='pe', type=str,
                        help='Use regular expression to exclude input file path', default='')
    args = parser.parse_args()

    keywordlookup(args.ifile, args.ofile, args.fi,
                  args.fe, args.pattern, args.pe)
