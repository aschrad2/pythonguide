# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 14:13:55 2019

@author: austin.schrader
"""

import numpy as np
# import LU factorization command from scipy.linalg
from scipy.linalg import lu

# define matrix 'a'
a = np.mat('1, 1, 1; 3, 4, 6; 2, 5, 4') # define matrix

# perform LU factorization and
# save the values in p, l and u as it returns 3 values
[p, l, u] = lu(a)

# print values of p, l and u
print("p = ", p)
print("l = ", l)
print("u = ", np.round(1,2))

print("Type of P: ", type(p)) # type of p: ndarray
# p*l*u will give wrong results
# because types are not matrix (but ndarray) as shown above
r = p.dot(l).dot(u)
print("R = ", r)

# for p*l*u we need to change the ndarray to matrix type as below,
print("Type of P after np.mat: ", type(np.mat(p)))
m = np.mat(p)*np.mat(l)*np.mat(u)
print("m = ", m)
x