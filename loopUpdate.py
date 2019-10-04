# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:17:27 2019

@author: austin.schrader
"""

# loopUpdate.py

animals = ['tiger', 'cat', 'dog']
am = animals.copy()

# below line will go in infinite loop
# for a in animals:
for a in am:
    if len(a) > 3:
        animals.append(a)
        
print(animals)


animals = ['tiger', 'cat', 'dog']

for a in animals[:]:
    if len(a) > 3:
        animals.append(a)

print(animals)
