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


def f(x):
    u=1.0
    l=0.5
    g=9.81
    M=1.0
    m=0.1
    
    ff = [  x[1],
            m*np.sin(x[2])*(-l*x[3]**2+g*np.cos(x[2]))/(M+m*np.sin(x[2])**2)+1/(M+m*np.sin(x[2])**2)*u,
            x[3],
            np.sin(x[2])*(-m*l*x[3]**2*np.cos(x[2])+g*(M+m))/(M*l+m*l*np.sin(x[2])**2)+np.cos(x[2])/(M*l+l*m*np.sin(x[2])**2)*u
            ]
    
    return ff


x = [0.3,5.0,np.pi/4.0,5.5]

foo_ad = adfun(f,x)

foo_ad.init_reverse_jac()

J = foo_ad.jac_reverse(x)

print "REVERSE"
print 'ADPY J = \n',J

foo_ad.init_forward_jac()


J = foo_ad.jac_forward(x)

print "FORWARD"
print 'ADPY J = \n',J

