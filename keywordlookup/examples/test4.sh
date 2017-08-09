#!/usr/bin/env bash

python ../keywordlookup_file.py -i '~/Documents/v6/ct/' -o output_app_1 -fe '\.pyc$|^([^.]+)$|.png$|.gz|.java' -pe '/assets/(images)/|/translations/' -pf './test_input'
rm output_app_1_tmp_