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
        total_size = sum(dimension_size_result.itervalues())
        for k in sorted_names:
            print("{} : {} : percent {}".format(k, dimension_size_result[k], round((dimension_size_result[k] + 0.0) / total_size, 4)))

        print ("total size is {}.".format(total_size))


if __name__ == '__main__':
    main()
