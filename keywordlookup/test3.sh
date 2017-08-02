#!/usr/bin/env bash

python js_java.py -i '/home/liushu/venv/lib/python2.7/site-packages/flask_appbuilder/' -o output_js_app_1 -fe '\.pyc$|^([^.]+)$|.png$|.gz' -pe '/assets/(images)/|/translations/' -pf './test_iput'