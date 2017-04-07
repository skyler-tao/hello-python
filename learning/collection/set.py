#!/usr/bin/env python
# -*- coding: utf-8 -*-

new_set = set([1, 3, 4, 2])
print new_set
new_set.add(6)
print new_set
new_set.remove(1)
print new_set
one_set = set([1, 2, 3])
another_set = set([2, 3, 4])
print one_set & another_set     # 集合的交集
print one_set | another_set     # 集合的并集
