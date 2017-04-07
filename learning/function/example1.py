#!/usr/bin/env python
# -*- coding: utf-8 -*-


def change_list(input_list):
    input_list[0] = 'Changed'
    return input_list

my_list = [1, 3, 5]
change_list(my_list)
print my_list

other_list = [2, 4, 6]
change_list(other_list[:])
print other_list
