#!/usr/bin/env bash

python ../keywordlookup_file.py -i '~/PycharmProjects/incubator-superset/superset/' -o output_js_1 -fe '\.pyc$|^([^.]+)$|.png$|.gz' -pe '/assets/(images|dist|node_modules)/|/translations/' -pf './test_iput'
rm output_js_1_tmp_
