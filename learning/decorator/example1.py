#!/usr/bin/env python
# -*- coding: utf-8 -*-


def log(func):
    def wrapper(*args, **kw):           # * 代表元组， ** 代表字典
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper


@log
def now():
    print '2017-04-06'

now()
