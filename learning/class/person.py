#!/user/bin/env python
# -*- coding: utf-8 -*-


class Person:

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print "Hello, world! I'm %s." % self.name
