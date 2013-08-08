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

from __future__ import division

import numpy as np
try:
    import sympy as sp
except ImportError:
    print 'no sympy support'
    pass

import types

from adfloat import adfloat
from globalfuncs import *
from library import GRAPH_LIBRARY, FORWARD_J_LIBRARY1, FORWARD_J_LIBRARY2, REVERSE_J_LIBRARY1, REVERSE_J_LIBRARY2


class adfun:
    def __init__(self,fun,var,SYMPY=False):
        self.fun = fun
        self.var = var

        self.FORWARD = False
        self.REVERSE = False
        if SYMPY:
            self.sympy_fun = fun
            self.fun = self.sympy_evalf
            #self.sympy_dic = dict(zip(var[0],var[1]))

            self.var = var[1]
            self.sympy_x = var[0]

        self.graph_init()


    def graph_init(self):

            #init
            
            self.graph = {}
            self.graph_list = []
            self.v_dic = {}
            self.x_list=[]
            self.v = []
            self.index=0
            self.graphfoo = []
            
            #graph
            self.graphfoo.append("from __future__ import division")
            self.graphfoo.append("from numpy import array,sin,cos,tan,log,exp,sqrt,arcsin,arccos,arctan")
            self.graphfoo.append("def f(self,x):")
            self.graphfoo.append("    v = []")

            for i,vv in enumerate(self.var):

                #graph
                idd='v%i' %self.index
                self.v_dic[idd]=self.index
                self.x_list.append(adfloat(vv,parentfoo=self,idd = idd))
                self.graphfoo.append("    %s= x[%i]" % (idd,i))
                self.graphfoo.append("    v.append(%s)" % idd)
                self.index +=1

            R = self.fun(self.x_list)
            
            temp1 = map(str,R)

            self.graphfoo.append("    self.v = v")

            self.graphfoo.append("    return array([%s])" % ','.join(temp1))

            self.return_list = temp1
            self.J_dim = [len(self.return_list),len(self.var)]


            self.make_function(self.graphfoo,'f')
        
    def init_forward_jac(self):

        
        self.graphforward = []

        #forward
        self.graphforward.append("from __future__ import division")
        self.graphforward.append("from numpy import array,sin,cos,tan,log,exp,sqrt,arcsin,arccos,arctan,log10")
        self.graphforward.append("def forward_one_row(self,x_f):")
        self.graphforward.append("    v = self.v")
        #init

        self.forward_seed = np.eye(self.J_dim[1])

        for vv in self.x_list:

            idd = vv.idd
            i = self.v_dic[idd]
            #forward
            idd_f= '%s_f' % idd
            self.graphforward.append("    %s= x_f[%s]" % (idd_f,i))
            self.graphforward.append("    %s= self.v[%s]" % (idd,i))

#########################################################################################
        for GG in self.graph_list:
            op,va = GG
            v1,v2 = map(str,va)
            v3 = self.graph['%s%s' % (op,va)].idd

            self.graphforward.append("    %s=v[%s]" %(v3,self.v_dic[v3]) )

            if isinstance( va[1], adfloat ):
                v2_f = '%s_f' % v2
                self.graphforward.append(FORWARD_J_LIBRARY1[op](v3, '%s_f' % v3, v1 ,'%s_f' % v1, v2, v2_f ))
            else:
                self.graphforward.append(FORWARD_J_LIBRARY2[op](v3, '%s_f' % v3, v1 ,'%s_f' % v1, v2 ))
############################################################################################

        self.graphforward.append("    return array([%s_f])" % '_f,'.join(self.return_list))

        self.make_function(self.graphforward,'forward_one_row')


    def init_reverse_jac(self):

        self.graphreverse = []

        self.reverse_v_init_set = set()
        ret = []

        self.reverse_seed = np.eye(self.J_dim[0])    
        
        for vv in self.x_list:
            self.reverse_v_init_set.add('%s_r' % vv)

#########################################################################################
        for GG in self.graph_list:
            op,va = GG
            v1,v2 = map(str,va)
            v3 = self.graph['%s%s' % (op,va)].idd

            self.reverse_v_init_set.add('%s_r' % v1)

            if isinstance( va[1], adfloat ):
                v2_r = '%s_r' % v2
                self.reverse_v_init_set.add(v2_r)
                self.graphreverse.append(REVERSE_J_LIBRARY1[op](v3, '%s_r' % v3, v1 ,'%s_r' % v1, v2, v2_r ))
            else:
                self.graphreverse.append(REVERSE_J_LIBRARY2[op](v3, '%s_r' % v3, v1 ,'%s_r' % v1, v2 ))
            
############################################################################################


        for vv in self.x_list:
            ret.append(vv.idd) 
            
        self.graphreverse.insert(0,"    return array([%s_r])" % '_r,'.join(ret))

        for vv in self.v_dic:
            self.graphreverse.append("    %s= v[%s]" % (vv,self.v_dic[vv]))

        for i,dd in enumerate(self.return_list):
            self.graphreverse.append("    %s_r= x_r[%s]" % (dd,i))

        for vv in self.reverse_v_init_set:
            self.graphreverse.append("    %s = 0.0" % vv)

        self.graphreverse.append("    v = self.v")
        self.graphreverse.append("def reverse_one_column(self,x_r):")
        self.graphreverse.append("from numpy import array,sin,cos,tan,log,exp,sqrt,arcsin,arccos,arctan,log10")
        self.graphreverse.append("from __future__ import division")


        self.make_function(self.graphreverse[::-1],'reverse_one_column')

    
    def add_step(self,op,va,AA):
        
        
        #md = md5('%s%s' % (op,va)).hexdigest()
        
        md = '%s%s' % (op,va)
        try: 
            return self.graph[md]
        except KeyError:
            v3 = AA.idd = 'v%s' % self.index
            self.v_dic[v3] = self.index
            self.graph[md] = AA
            self.graph_list.append((op,va))
            v1,v2 = map(str,va)
            
            self.graphfoo.append(GRAPH_LIBRARY[op](v3,v1,v2))
            self.graphfoo.append("    v.append(%s)" % v3)

            self.index +=1

            return AA


    def make_function(self,graph,func_name):
        
        r = '\n'
        code = compile(r.join(graph),'<string>', 'exec')
        NN = {}
        exec code in NN
        setattr(self, func_name, types.MethodType(NN[func_name], self))

    #@profile
    def jac_forward(self,x):
        if not self.forward_one_row:
            print 'Forward mode had not been initialized'
            return

        self.F = self.f(x)
        self.J = np.empty(self.J_dim)
        for i in xrange(self.J_dim[1]):

            self.J[:,i] = self.forward_one_row(self.forward_seed[i,:])

        return self.J

    def jac_reverse(self,x):
        if not self.reverse_one_column:
            print 'Reverse mode had not been initialized'
            return

        self.F = self.f(x)
        self.J = np.empty(self.J_dim)

        for i in xrange(self.J_dim[0]):

            self.J[i,:] = self.reverse_one_column(self.reverse_seed[:,i])

        return self.J


    def sympy_evalf(self,x):

        GLSfoo = sp.lambdify(self.sympy_x,sp.Matrix(self.sympy_fun),modules='numpy')

        return GLSfoo(*x).flatten().tolist()[0]
        
        #funktioniert is aber langsamer
        # sympy_function = []
        # sympy_function.append("from __future__ import division")
        # sympy_function.append("from numpy import array,sin,cos,tan,log,exp")
        # sympy_function.append("def sympy_func(self,x):")

        # dic = dict(zip(self.sympy_x,x))

        # for i,vv in enumerate(x):
        #     sympy_function.append('    %s = x[%s]' % (vv,i))

        # f = self.sympy_fun
        # ss = map(str,[ff.subs(dic) for ff in f])
        
        # sympy_function.append("    f  =[]")

        # for sss in ss:
        #     sympy_function.append("    f.append(eval('%s'))" % sss)

        # sympy_function.append("    return f")

        # self.make_function(sympy_function,'sympy_func')
        # #IPS()
        # return self.sympy_func(x)


    def __call__(self,x):
        return self.f(x)