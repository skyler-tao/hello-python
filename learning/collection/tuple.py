#!/user/bin/env python
# -*- coding: utf-8 -*-


classmates = ('Michael', 'Jim', 'Tom', 'Tao', 'Skyler')
print classmates
t = (1, 2)
print t
one_tuple = (6,)
print one_tuple
empty_tuple = ()
print empty_tuple
# 可变 tuple
inner_list = ['A', 'B', 'C']
mutable_tuple = ('a', 'b', inner_list, 'd')
print mutable_tuple
inner_list[2] = 'BB'
print mutable_tuple
