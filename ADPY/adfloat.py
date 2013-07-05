# coding: utf-8
from __future__ import division
import numpy as np
from ipHelp import IPS, ST, ip_syshook, dirsearch, sys


class adfloat:
    def __init__(self,value,parentfoo=None,idd=None):
        self.real=value
        self.parentfoo=parentfoo

        if idd:
            self.idd = idd
        else:
            self.idd = 'ID'+str(id(self))
            
    def __repr__(self):
        return  self.idd

    def __set__(self,value):
        self.real = value

    def op(self,operation,other=None):
        if other:
            AA = adfloat(operation(self.real,other.real),parentfoo=self.parentfoo)
            #sol =self.parentfoo.add_step(operation,[self,other],AA)
        else:
            AA = adfloat(operation(self.real),parentfoo=self.parentfoo)
            #sol =self.parentfoo.add_step(operation,[self],AA)

        sol =self.parentfoo.add_step(operation,[self,other],AA)
        return sol

    def __sub__(self,other):
        return self.op(np.subtract,other)

    def __rsub__(self,other):
        #irgendwas geht hier schief
        return self.op(np.float.__rsub__,other)
        
    def __add__(self,other):
        return self.op(np.add,other)

    def __radd__(self,other):
        return self.__add__(other)

    def __mul__(self,other):
        return self.op(np.multiply,other)

    def __rmul__(self,other):
        return self.__mul__(other)

    def __div__(self,other):
        return self.op(np.divide,other)

    def __rdiv__(self,other):
        return self.op(np.float.__rdiv__,other)

    def __pow__(self,other):
        return self.op(np.power,other)

    def __rpow__(self,other):
        return self.op(np.float.__rpow__,other)

    def __neg__(self):
        return self.op(np.negative)

    def cos(self):
        return self.op(np.cos)

    def sin(self):
        return self.op(np.sin)
    
    def tan(self):
        return self.op(np.tan)

    def exp(self):
        return self.op(np.exp)

    def arcsin(self):
        #IPS()
        return self.op(np.arcsin)

    def arccos(self):
        return self.op(np.arccos)

    def arctan(self):
        return self.op(np.arctan)

    def sqrt(self):
        return self.op(np.sqrt)

    def log(self):
        return self.op(np.log)

    def log10(self):
        return self.op(np.log10)

    __truediv__ = __div__
    __rtruediv__ = __rdiv__