#!/usr/bin/env python
# -*- coding: utf-8 -*-

# dict 中存放的 key 的顺序与放入的顺序无关
name_score = {'Michael': 98, 'Bob': 87, 'Tao': 99, 'Skyler': 100}
print name_score
print name_score['Tao']
name_score['Adam'] = 66
print name_score

if 'Jim' in name_score:
    print name_score['Jim']
else:
    print 'Not exist Jim in name_score.'
name_score.pop('Skyler')
print name_score
