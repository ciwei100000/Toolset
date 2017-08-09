# -*- coding:utf-8 -*-

from keywordlookup import keywordlookup

import argparse
import os


def keywordjs(ifile, ofile, fi, fe, patternfile, pe):

    ifile = os.path.expanduser(os.path.expandvars(ifile))
    ofile = os.path.expanduser(os.path.expandvars(ofile))

    with open(patternfile, 'r') as f:
        with open(ofile, 'w') as w:
            for line in f:
                print line
                keywordlookup(ifile, ofile + '_tmp_', fi, fe, line, pe)
                with open(ofile + '_tmp_', 'r') as r:
                    w.write(line + '\n')
                    w.write(r.read())
                    w.write('\n\n')


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
    parser.add_argument('--patternfile', '-pf', dest='patternfile', type=str,
                        help='The file containing regular expressions to define the pattern to look for',
                        default='_\(["\']')
    parser.add_argument('--path_exclude_rule', '-pe', dest='pe', type=str,
                        help='Use regular expression to exclude input file path', default='')
    args = parser.parse_args()

    keywordjs(args.ifile, args.ofile, args.fi, args.fe, args.patternfile, args.pe)
