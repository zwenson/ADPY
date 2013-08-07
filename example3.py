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
import sympy as sp

x1,x2,x3  =sp.symbols('x1 x2 x3')

x=np.array([x1,x2,x3])

GLS = [ x2+x3-5,
        -x1**2 +x3 +1, 
        -x2 + sp.cos(x1) -x3 + 7]

x0=np.array([100.0,1.0,1.0])

x_tupel = (x,x0)
foo_ad = adfun(GLS,x_tupel,SYMPY=True)

p = foo_ad([1,2,3])

print "p = ", p
