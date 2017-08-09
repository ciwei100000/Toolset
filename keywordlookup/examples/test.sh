#!/usr/bin/env bash
python ../keywordlookup.py -i '~/PycharmProjects/incubator-superset/superset' -o output_superset -fe '\.pyc$|^([^.]+)$|.png$|.gz' -pe '/assets/(node_modules|images|dist)/|/translations/'
python ../keywordlookup.py -i '~/PycharmProjects/incubator-superset/superset' -o output_superset -fe '\.pyc$|^([^.]+)$|.png$|.gz' -pe '/assets/(node_modules|images|dist)/|/translations/'
cat output_superset > output
cat output_appbuilder >> output
