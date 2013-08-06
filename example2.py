# coding: utf-8


#see http://www.mathworks.com/help/optim/ug/fsolve.html

from ADPY import adfun
from ADPY import solver
import numpy as np
import sympy as sp


x1,x2  =sp.symbols('x1 x2')
x=np.array([x1,x2])
    
F = [2*x1 - x2 - sp.exp(-x1),
    -x1 + 2*x2 - sp.exp(-x2)]
        
x0 = [-5, -5]

Solver = solver(F,x0,x=x,algo='leven',tol=1e-10,maxx=100)
sol = Solver.solve()

print sol