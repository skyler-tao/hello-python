#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 根据 druid 导入的 etl-zhihu 字段，找出现有后端无效的维度信息

import json
import pprint


def main():
    druid_dimensions_set = set()
    za_dimensions_set = set()

    with open('druid_dimensions.json') as druid_dimensions_raw:
        druid_dimensions = json.load(druid_dimensions_raw)
        for druid_dimension in druid_dimensions:
            if isinstance(druid_dimension, basestring):
                druid_dimensions_set.add(druid_dimension)
            else:
                druid_dimensions_set.add(druid_dimension['name'])
    with open('za_dimensions.json') as za_dimension_raw:
        za_dimensions = json.load(za_dimension_raw)
        for za_dimension in za_dimensions:
            za_dimensions_set.add(za_dimension['propertyName'])

    druid_difference = druid_dimensions_set.difference(za_dimensions_set)
    pprint.pprint(druid_difference)

    za_difference = za_dimensions_set.difference(druid_dimensions_set)
    pprint.pprint(za_difference)


if __name__ == '__main__':
    main()
