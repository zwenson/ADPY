# coding: utf-8

""" 
    Copyright 2013 Oliver Schnabel
    
    This file is part of ADPY.
    ADPY is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    ADPY is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with ADPY.  If not, see <http://www.gnu.org/licenses/>.
"""

from ADPY import adfun
import numpy as np
from time import clock


def f(x):
    x1,x2,x3,x4,x5 = x
    return np.array([
            np.arccos(np.sqrt(1/np.log(1/x1**2*np.cos(np.arccos(1/x2))+x3**3))),
            -np.log(x1**2*np.cos(np.arccos(1/x2))+x3**3),
            3/x5**2*np.cos(x5**2),
            np.arctan(x1**2*np.cos(np.arccos(1/x2)))**x4/(3/x5**2*np.cos(x5**2))
            ])
    

x1 = np.array([1.,2.,3.,4.,5.])

AD = adfun(f,x1)

t1 = clock()
for i in xrange(10000):
    y = 0
    y = f(x1)
    
print "Built-in function took", clock()-t1, "s"
print y

t1 = clock()
for i in xrange(10000):
    y = 0
    y = AD(x1)
    
print "ADPY computational graph took", clock()-t1, "s"
print y




