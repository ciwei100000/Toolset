#!/usr/bin/env bash

python js_java.py -i '/home/liushu/PycharmProjects/incubator-superset/superset/' -o output_js_1 -fe '\.pyc$|^([^.]+)$|.png$|.gz' -pe '/assets/(images|dist|node_modules)/|/translations/' -pf './test_iput'