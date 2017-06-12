#!/usr/bin/env python
# -*- coding: utf-8 -*-


import json

with open('servers_simple_info.json') as druid_historical_info:
    historical_info = json.load(druid_historical_info)
    for info in historical_info:
        type = info['type']
        if ('historical' == type):
            print info['host']
    print historical_info
