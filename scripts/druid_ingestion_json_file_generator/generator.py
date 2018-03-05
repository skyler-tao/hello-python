#!/user/bin/env python
# encoding: utf-8

import pprint
import json


def main():
    with open('input.txt') as data_file:
        fields = list()
        for line in data_file:
            origin_str = line.split('as ')[0].strip(' ')
            field = dict()
            field['expr'] = '$.' + origin_str
            field['name'] = origin_str
            field['type'] = 'path'
            fields.append(field)

        result = json.dumps(fields)
        print(result)


if __name__ == '__main__':
    main()
