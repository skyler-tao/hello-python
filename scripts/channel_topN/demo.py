#!/user/bin/env python
# encoding: utf-8

import pprint
import json


def main():
    target_column = 'package_name'
    column_set = set()
    column_count = dict()
    with open('channel_info.json') as channel_info:
        channel_info_json = json.load(channel_info)
        channel_info_data = channel_info_json['data']
        pprint.pprint(len(channel_info_data))
        for info in channel_info_data:
            column_value = info[target_column]
            column_set.add(column_value)
            if column_value in column_count:
                column_count.update({column_value: column_count.get(column_value) + 1})
            else:
                column_count.update({column_value, 1})
        pprint.pprint(len(column_set))


if __name__ == '__main__':
    main()
