# coding: utf-8

from ADPY import adfun
import numpy as np
import sympy as sp

x1,x2,x3  =sp.symbols('x1 x2 x3')

x=np.array([x1,x2,x3])

GLS = [ x2+x3-5,
        -x1**2 +x3 +1, 
        -x2 + sp.cos(x1) -x3 + 7]
        #x1**2 +x2**2]

#x0=list([-1.1,9,-3])
x0=np.array([100.0,1.0,1.0])

x_tupel = (x,x0)
foo_ad = adfun(GLS,x_tupel,SYMPY=True)
# foo_ad.graph_only()

p = foo_ad([1,2,3])

print "p = ", p
