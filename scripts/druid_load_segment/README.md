## 介绍
排查 coordinator UI 上 loadstatus 不为 100 的情况的 segments 数据

## 使用
确定一个数据源：${dataSource}
首先调用 `http://coordinator-web-host/druid/coordinator/v1/datasources/${dataSource}/intervals?simple`
获取到 loaded segments 列表，将返回的 json 放入 loaded_segments.json 文件中。

然后查询 druid mysql 数据，如：
```
mysql -h mysql_host -P 31807 -u druid -p**** druid -e"select id from druid_segments where dataSource='topic_metrics' and used=1;" > temp.txt
```

然后本地通过 sftp 将查询出来的结果去除第一行的 id ，将所有的 segment_id 文本放入 segments_in_db.txt 文件中。

修改 load_segment_diff.py 文件中的 data_source 变量为指定的 ${dataSource}，执行 main 方法。

根据返回的 diff 结果，查看 HDFS 文件是否 ready.

举例：
数据库中是：
hdfs://hdfs-host/data/druid/segments/topic_metrics/20171107T000000.000Z_20171107T010000.000Z/2017-11-08T00_32_48.253Z/0/index.zip