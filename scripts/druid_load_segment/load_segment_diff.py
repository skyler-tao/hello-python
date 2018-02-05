#!/user/bin/env python
# encoding: utf-8

import pprint
import os.path


def main():

    global my_path
    my_path = os.path.abspath(os.path.dirname(__file__))

    data_source = 'tmp_db_duration_info'
    loaded_segments = get_loaded_segments(data_source)

    pprint.pprint("loaded segments size: " + str(len(loaded_segments)))

    segments_in_db = get_db_segments()

    pprint.pprint("db segments size: " + str(len(segments_in_db)))

    diff = segments_in_db.difference(loaded_segments)

    pprint.pprint("diff segments size: " + str(len(diff)))
    pprint.pprint(diff)


# 统一格式 dataSource_startTime_endTime
def get_loaded_segments(data_source):
    path = os.path.join(my_path, "loaded_segments.json")
    with open(path) as input_file:
        import json
        loaded_segments = json.load(input_file)
        segment_ids = set()
        for json in loaded_segments:
            json = json.replace('/', '_')
            json = data_source + "_" + json
            segment_ids.add(str(json))
        return segment_ids


# 统一格式 dataSource_startTime_endTime
def get_db_segments():
    path = os.path.join(my_path, "segments_in_db.txt")
    with open(path) as input_file:
        segment_ids = set()
        for line in input_file:
            line = line.replace('\n', '')
            # 去除数据库中的数据版本
            segment_ids.add(line[0:-25])
        return segment_ids


if __name__ == '__main__':
    main()
