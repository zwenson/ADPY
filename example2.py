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
from ADPY import solver
import numpy as np
try:
    import sympy as sp
    SYMPY_SUPPORT = True
except ImportError:
    print 'no sympy support'
    SYMPY_SUPPORT = False
    pass

###### example2 #######
"""
see http://www.mathworks.com/help/optim/ug/fsolve.html for example

    - Solving a system of nonlinear equation of type F(x) = 0
    - provide either a callable function or a sympy expression
    - solver supoorts Levenberg–Marquardt algorithm ('leven'),
      Gauss–Newton algorithm ('gauss'), Newton algorithm ('newton')
    - Automatic differentiation is used to obtain derivatives
    - see solver class for more information
"""


##### as function ####

#provide a callable function
def f(y):
    return [2*y[0] - y[1] - np.exp(-y[0]),
            -y[0] + 2*y[1] - np.exp(-y[1])]

# a start value
y0 = [-5, -5]

#create Solver
Solver1 = solver(f,y0,algo='newton',tol=1e-10,maxx=100)
#Solver1 = solver(f,y0,algo='gauss',tol=1e-10,maxx=100)
#Solver1 = solver(f,y0,algo='leven',tol=1e-10,maxx=100)

sol = Solver1.solve()

print sol


##### with sympy ######

if SYMPY_SUPPORT == False:
    exit()

# create symbols and put them in an array
x1,x2  =sp.symbols('x1 x2')
x=np.array([x1,x2])

# the equation system
F = [2*x1 - x2 - sp.exp(-x1),
    -x1 + 2*x2 - sp.exp(-x2)]

#start value
x0 = [-5, -5]

#create Solver
Solver2 = solver(F,x0,x=x,algo='leven',tol=1e-10,maxx=100,SYMPY=True)
sol = Solver2.solve()

print sol
