# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:09:29 2019

@author: austin.schrader
"""
# arrayEx.py

import numpy as np

a = np.array([1, 8, 2])
print(a) # [1 8 2] 
print(np.shape(a)) # (3,)

b = np.array([
        [1,2],
        [4,3],
        [6,2]
])

# b can be written as follow as well, but above is more readable
# b=np.array([[1,2],[4,3]])
print(np.shape(b)) #(3,2) i.e. 3 row and 2 column

# row of array can have different number of elements
c=np.array([[np.arange(1,10)],[np.arange(11,16)]])
print(c)
