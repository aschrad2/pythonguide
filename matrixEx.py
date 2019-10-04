# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:11:34 2019

@author: austin.schrader
"""

# matrixEx.py

import numpy as np
from scipy.linalg import lu

a = np.mat('1, 2; 3, 2; 2, 3') # define matrix
print(np.shape(a)) # (3,2)

aT = np.transpose(a) # transpose of matrix 'a'
print(np.shape(aT)) # (2, 3)

# eye(n) is used for (nxn) identify matrix
b = 2*np.eye(3) # 2*identify matrix
print(np.shape(b)) # (3,3)

c = b*a
print(np.shape(c)) # (3,2)

l = lu(a)
print(l)