#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pprint


def main():
    used_dimensions_set = set()

    with open('reports_error.json') as reports_all_raw:
        used_dimensions_list = list()
        reports_all = json.load(reports_all_raw)
        for report in reports_all:
            if 'queries' in report and len(report['queries']) > 0:
                product_id = report['queries'][0]['product']
                if product_id == 1:
                    queries = report['queries']
                    for query in queries:
                        if 'filter' in query:
                            dimensions = get_filter_dimension(query['filter'])
                            used_dimensions_list.append(dimensions)
                        if 'dimensions' in query:
                            used_dimensions_list.append(query['dimensions'])
    pprint.pprint(used_dimensions_list)
    used_dimensions_list = deep_flatten(used_dimensions_list)
    pprint.pprint(used_dimensions_list)


def get_filter_dimension(filter_body):
    if filter_body is None:
        return None

    if 'type' in filter_body:
        if filter_body['type'] in ('selector', 'regex', 'begin', 'end', 'contain'):
            return filter_body['dimension']
        elif filter_body['type'] in ('and', 'or'):
            dimension_list = list()
            for sub_filter in filter_body['filters']:
                sub_dimension = get_filter_dimension(sub_filter)
                if sub_dimension is not None:
                    dimension_list.append(sub_dimension)
            return dimension_list
        elif filter_body['type'] == 'not':
            return get_filter_dimension(filter_body['filter'])
        else:
            return None
    else:
        return None


def deep_flatten(input_list):
    if not isinstance(input_list, list) or is_level_one(input_list):
        return input_list

    if is_level_two(input_list):
        return [value for elem in input_list for value in elem]
    else:
        flatten_list = list()
        for element in input_list:
            flatten_list.append(deep_flatten(element))
        return flatten_list


def is_level_one(input_list):
    if not isinstance(input_list, list):
        return True
    for element in input_list:
        if isinstance(element, list):
            return False


# todo
def is_level_two(input_list):
    if not isinstance(input_list, list) or is_level_one(input_list):
        return False

    for element in input_list:
        if not isinstance(element, list) or is_level_one(element):
            continue


if __name__ == '__main__':
    main()
