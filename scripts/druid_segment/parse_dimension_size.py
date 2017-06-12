#!/user/bin/env python
# encoding: utf-8

import pprint


def main():
    with open('meta.smoosh') as data_file:
        line_index = 0
        dimension_size_result = {}
        for line in data_file:
            line_index += 1
            if line_index < 3:
                continue

            elements = line.split(',')
            dimension_name = elements[0]
            dimension_size = int(elements[len(elements) - 1]) - int(elements[len(elements) - 2])
            dimension_size_result[str(dimension_name)] = int(dimension_size)
        sorted_names = sorted(dimension_size_result, key=lambda x: dimension_size_result[x])
        for k in sorted_names:
            print("{} : {}".format(k, dimension_size_result[k]))


if __name__ == '__main__':
    main()
