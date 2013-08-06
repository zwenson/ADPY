# coding: utf-8

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


x = [0.5,0.5,np.pi,0.5]

foo_ad = adfun(f,x)
print '\n######## ADDYN #########\n'

foo_ad.init_reverse_jac()

J = foo_ad.jac_reverse(x)

print "REVERSE"
print 'ADPY J = \n',J

foo_ad.init_forward_jac()


J = foo_ad.jac_forward(x)

print "FORWARD"
print 'ADPY J = \n',J

