# coding: utf-8

from time import clock

import sys
sys.path.append('/home/zwen/myModules')
from ipHelp import IPS, ST, ip_syshook, dirsearch, sys

from adpy2 import *

#import algopy
#from algopy import UTPM
import numpy as np
import sympy as sp

x=[0.8,0.6,0.5,0.4,0.3,30]

def f(x):

    #ff = x[0]-x[1]
    #ff = np.cos(x[0])
    #ff = [x[0]-x[1], x[0]/x[1]]
    #ff = [x[0],x[1]**3]
    ff = [np.log(x[0]),np.arcsin(x[0])* np.arccos(x[1]),np.exp(x[2])*np.sqrt(x[3]),np.arctan(x[4])*np.log(x[5]),x[2]/x[3],np.log(np.sqrt(x[1]))]
    #ff = [1+x[0],(x[0])*(x[1]),(x[2])*(x[3])*(x[4])*((x[1]))]
    #ff = [(2*x[0]**2+2)*np.cos(x[0]**2)/(2+np.cos(x[0]**2)+1) , np.cos(x[1]**2)/np.tan(x[1]/x[0])**x[1]] #
    #ff = [(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)**2*(x[0]*x[1])**10/(x[0]*np.cos(x[1]))**10*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)**2*(x[0]*x[1])**10/(x[0]*np.cos(x[1]))**10*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)**2*(x[0]*x[1])**10/(x[0]*np.cos(x[1]))**10*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)**2*(x[0]*x[1])**10/(x[0]*np.cos(x[1]))**10*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)*(x[0]-x[1]-1)**2*(x[0]*x[1])**10/(x[0]*np.cos(x[1]))**10]
    #IPS()
    return ff


def main():
    

    foo_ad = adfun(f,x)
    # foo_ad.graph_only()

    # print 'DONE INIT'

    # x = [6.0,2.0]

    # t1 = clock()
    # for i in range(10000):
    #     y_f  = np.array(foo_ad.fun(x))    

    # print 'y_f   =',y_f,'   time:',clock()-t1
    # t1 = clock()

    # for i in range(10000):

    #     y_ad = foo_ad(x)

    # print 'y_ad  =',y_ad,'   time:',clock()-t1

    # print 'FORWARD'


    import algopy
    from algopy import UTPM
    n=len(f(x))
    def F(args): #Arugmente auspacken und func aufrufen
        #a little wrapper due the behavior of lambdify
        out = algopy.zeros(n, dtype=args)
        G = f(args)
        for i in range(n):
            out[i]=G[i]
        return out
    x1 = UTPM.init_jacobian(x)
    y = F(x1)
    algopy_jacobian = UTPM.extract_jacobian(y)
    print 'jacobian = \n',algopy_jacobian


    print '\n######## ADDYN #########\n'
    foo_ad.init_forward_jac()
    print foo_ad(x)

    t1 = clock()
    for i in xrange(1):

        J = foo_ad.jac_forward(x)

    print 'ADPY J = \n',J,'\ntime:',clock()-t1

    IPS()

def test_sympy():
    x1,x2,x3  =sp.symbols('x1 x2 x3')

    x=np.array([x1,x2,x3])

    GLS = [ x2+x3-5,
            -x1**2 +x3 +1, 
            -x2 + sp.cos(x1) -x3 + 7]
            #x1**2 +x2**2]

    #x0=list([-1.1,9,-3])
    x0=np.array([100.0,1.0,1.0])

    x_dic = dict(zip(x,x0))

    x_tupel = (x,x0)
    foo_ad = adfun(GLS,x_tupel,SYMPY=True)
    foo_ad.graph_only()

    p = foo_ad([1,2,3])

    IPS()
def reverse():
    x = [1,2]

    def fr(y):
        return [y[0]-y[1],y[0]*y[1]]

    foo_ad = adfun(fr,x)
    print '\n######## ADDYN #########\n'
    foo_ad.init_reverse_jac()

    t1 = clock()
    for i in xrange(1000):

        J = foo_ad.jac_reverse(x)

    print "REVERSE"
    print 'ADPY J = \n',J,'\ntime:',clock()-t1

    foo_ad.init_forward_jac()

    t1 = clock()
    for i in xrange(1000):

        J = foo_ad.jac_forward(x)

    print "FORWARD"
    print 'ADPY J = \n',J,'\ntime:',clock()-t1
    
    IPS()

#if __name__ == '__main__':
#print f(x)
reverse()
#main()
#test_sympy()
