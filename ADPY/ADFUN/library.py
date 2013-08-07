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

import numpy as np
##############################################################################

#                   GRAPH

##############################################################################
GRAPH_LIBRARY= {}
#v3 = v1 -v2
GRAPH_LIBRARY[np.subtract]              =lambda v3,v1,v2:"    %s=%s-%s"    %(v3,v1,v2)
GRAPH_LIBRARY[np.float.__rsub__]        =lambda v3,v1,v2:"    %s=%s-%s"    %(v3,v2,v1)
#v3 = v1 +v2
GRAPH_LIBRARY[np.add]                   =lambda v3,v1,v2:"    %s=%s+%s"    %(v3,v1,v2)
#v3 = v1 * v2
GRAPH_LIBRARY[np.multiply]              =lambda v3,v1,v2:"    %s=%s*%s"    %(v3,v1,v2)
#v3 = v1 / v2
GRAPH_LIBRARY[np.divide]                =lambda v3,v1,v2:"    %s=%s/%s"    %(v3,v1,v2)
GRAPH_LIBRARY[np.float.__rdiv__]        =lambda v3,v1,v2:"    %s=%s/%s"    %(v3,v2,v1)
#v3 = cos(v1)
GRAPH_LIBRARY[np.cos]                   =lambda v3,v1,v2:"    %s=cos(%s)"  %(v3,v1)
#v3 = sin(v1)
GRAPH_LIBRARY[np.sin]                   =lambda v3,v1,v2:"    %s=sin(%s)"  %(v3,v1)
#v3 = tan(v1)
GRAPH_LIBRARY[np.tan]                   =lambda v3,v1,v2:"    %s=tan(%s)"  %(v3,v1)
#v3 = v1 ** v2
GRAPH_LIBRARY[np.power]                 =lambda v3,v1,v2:"    %s=%s**%s"   %(v3,v1,v2)
#v3 = v1 ** v2
GRAPH_LIBRARY[np.float.__rpow__]        =lambda v3,v1,v2:"    %s=%s**%s"   %(v3,v2,v1)
#v3_f = exp(v1)
GRAPH_LIBRARY[np.exp]                   =lambda v3,v1,v2:"    %s=exp(%s)"  %(v3,v1)
#v3_f = arcsin(v1)
GRAPH_LIBRARY[np.arcsin]                =lambda v3,v1,v2:"    %s=arcsin(%s)"  %(v3,v1)
#v3_f = arccos(v1)
GRAPH_LIBRARY[np.arccos]                =lambda v3,v1,v2:"    %s=arccos(%s)"  %(v3,v1)
#v3_f = arctan(v1)
GRAPH_LIBRARY[np.arctan]                =lambda v3,v1,v2:"    %s=arctan(%s)"  %(v3,v1)
#v3_f = sqrt(v1)
GRAPH_LIBRARY[np.sqrt]                  =lambda v3,v1,v2:"    %s=sqrt(%s)"  %(v3,v1)
#v3_f = log(v1)
GRAPH_LIBRARY[np.log]                   =lambda v3,v1,v2:"    %s=log(%s)"  %(v3,v1)
#v3_f = log10(v1)
GRAPH_LIBRARY[np.log10]                 =lambda v3,v1,v2:"    %s=log10(%s)"  %(v3,v1)
#v3_f=-v1
GRAPH_LIBRARY[np.negative]              =lambda v3,v1,v2:"    %s=-%s"   %(v3,v1)



##############################################################################

#                   FORWARD JACOBIAN

##############################################################################
FORWARD_J_LIBRARY1= {}

#v3_f = v1_f - v2_f
FORWARD_J_LIBRARY1[np.subtract]         =lambda v3,v3_f,v1,v1_f,v2,v2_f:"    %s=%s-%s"        %(v3_f,v1_f,v2_f)
#v3_f = v1_f + v2_f
FORWARD_J_LIBRARY1[np.add]              =lambda v3,v3_f,v1,v1_f,v2,v2_f:"    %s=%s+%s"        %(v3_f,v1_f,v2_f)
#v3_f = v1_f*v2 + v2_f*v1
FORWARD_J_LIBRARY1[np.multiply]         =lambda v3,v3_f,v1,v1_f,v2,v2_f:"    %s=%s*%s+%s*%s"  %(v3_f,v1_f,v2,v2_f,v1)
#v3_f = (v1_f + v3*v2_f)/v2
FORWARD_J_LIBRARY1[np.divide]           =lambda v3,v3_f,v1,v1_f,v2,v2_f:"    %s=(%s-%s*%s)/%s" %(v3_f,v1_f,v3,v2_f,v2)
#v3_f = v3 * (v1_f/v1 * v2 + ln(v1)*v2_f)
FORWARD_J_LIBRARY1[np.power]            =lambda v3,v3_f,v1,v1_f,v2,v2_f:"    %s=%s*(%s/%s*%s+log(%s)*%s)" %(v3_f,v3,v1_f,v1,v2,v1,v2_f)


#if va[1] not a adfloat
#-- v2_f = 0
FORWARD_J_LIBRARY2= {}

#v3_f = v1_f - v2_f
FORWARD_J_LIBRARY2[np.subtract]         =lambda v3,v3_f,v1,v1_f,v2:"    %s=%s"        %(v3_f,v1_f)
FORWARD_J_LIBRARY2[np.float.__rsub__]   =lambda v3,v3_f,v1,v1_f,v2:"    %s=-%s"        %(v3_f,v1_f)
#v3_f = v1_f + v2_f
FORWARD_J_LIBRARY2[np.add]              =lambda v3,v3_f,v1,v1_f,v2:"    %s=%s"        %(v3_f,v1_f)
#v3_f = v1_f*v2 + v2_f*v1
FORWARD_J_LIBRARY2[np.multiply]         =lambda v3,v3_f,v1,v1_f,v2:"    %s=%s*%s"      %(v3_f,v1_f,v2)
#v3_f = (v1_f + v3*v2_f)/v2
FORWARD_J_LIBRARY2[np.divide]           =lambda v3,v3_f,v1,v1_f,v2:"    %s=%s/%s"       %(v3_f,v1_f,v2)
FORWARD_J_LIBRARY2[np.float.__rdiv__]   =lambda v3,v3_f,v1,v1_f,v2:"    %s=-%s*%s/%s"   %(v3_f,v1_f,v3,v1)
#v3_f = -sin(v1)*v1_f
FORWARD_J_LIBRARY2[np.cos]              =lambda v3,v3_f,v1,v1_f,v2:"    %s=-sin(%s)*%s"  %(v3_f,v1,v1_f)
#v3_f = cos(v1)*vf_1
FORWARD_J_LIBRARY2[np.sin]              =lambda v3,v3_f,v1,v1_f,v2:"    %s=cos(%s)*%s"   %(v3_f,v1,v1_f)
#v3_f = (1 + v3**2)*v1_f
FORWARD_J_LIBRARY2[np.tan]              =lambda v3,v3_f,v1,v1_f,v2:"    %s=(1.0+%s**2)*%s" %(v3_f,v3,v1_f)
#v3_f = v3 * (v1_f/v1 * v2 + ln(v1)*v2_f)
FORWARD_J_LIBRARY2[np.power]            =lambda v3,v3_f,v1,v1_f,v2:"    %s=%s*(%s/%s*%s)" %(v3_f,v3,v1_f,v1,v2)
#v3_f = exp(v1)*v1_f
FORWARD_J_LIBRARY2[np.exp]              =lambda v3,v3_f,v1,v1_f,v2:"    %s=exp(%s)*%s"   %(v3_f,v1,v1_f)
#v3_f = 1/sqrt(1-x**2)
FORWARD_J_LIBRARY2[np.arcsin]           =lambda v3,v3_f,v1,v1_f,v2:"    %s=1.0/(sqrt(1-%s**2))*%s"   %(v3_f,v1,v1_f)
#v3_f = -1/sqrt(1-x**2)
FORWARD_J_LIBRARY2[np.arccos]           =lambda v3,v3_f,v1,v1_f,v2:"    %s=-1.0/(sqrt(1-%s**2))*%s"   %(v3_f,v1,v1_f)
#v3_f = 1/(v1**2+1)
FORWARD_J_LIBRARY2[np.arctan]           =lambda v3,v3_f,v1,v1_f,v2:"    %s=1.0/(%s**2+1)*%s"   %(v3_f,v1,v1_f)
#v3_f = 1/(2*v3)
FORWARD_J_LIBRARY2[np.sqrt]             =lambda v3,v3_f,v1,v1_f,v2:"    %s=1.0/(2*%s)*%s"   %(v3_f,v3,v1_f)
#v3_f = 1/(v1)*v1_f
FORWARD_J_LIBRARY2[np.log]              =lambda v3,v3_f,v1,v1_f,v2:"    %s=1.0/(%s)*%s"   %(v3_f,v1,v1_f)
#v3_f = 1/(v1 * log(10)*v1_f
FORWARD_J_LIBRARY2[np.log10]            =lambda v3,v3_f,v1,v1_f,v2:"    %s=1.0/(%s*log(10))*%s"   %(v3_f,v1,v1_f)
#v3_f = -v1_f
FORWARD_J_LIBRARY2[np.negative]         =lambda v3,v3_f,v1,v1_f,v2:"    %s=-%s"   %(v3_f,v1_f)
FORWARD_J_LIBRARY2[np.float.__rpow__]   =lambda v3,v3_f,v1,v1_f,v2:"    %s=%s*(log(%s)*%s)" %(v3_f,v3,v2,v1_f)

##############################################################################

#                   REVERSE JACOBIAN

##############################################################################

REVERSE_J_LIBRARY1 = {}

#v3 = v1 - v2
REVERSE_J_LIBRARY1[np.subtract]         =lambda v3,v3_r,v1,v1_r,v2,v2_r:"    %s+=%s \n    %s+=-%s"        %(v1_r,v3_r,v2_r,v3_r)
#v3 = v1 + v2
REVERSE_J_LIBRARY1[np.add]              =lambda v3,v3_r,v1,v1_r,v2,v2_r:"    %s+=%s \n    %s+=%s"        %(v1_r,v3_r,v2_r,v3_r)
#v3_f = v1_f*v2 + v2_f*v1
REVERSE_J_LIBRARY1[np.multiply]         =lambda v3,v3_r,v1,v1_r,v2,v2_r:"    %s+=%s*%s \n    %s+=%s*%s"  %(v1_r,v3_r,v2,v2_r,v3_r,v1)
#v3_f = (v1_f + v3*v2_f)/v2
REVERSE_J_LIBRARY1[np.divide]           =lambda v3,v3_r,v1,v1_r,v2,v2_r:"    %s+=%s/%s \n    %s+=-%s*%s/%s"  %(v1_r,v3_r,v2,v2_r,v3_r,v3,v2)
#v3_f = v3 * (v1_f/v1 * v2 + ln(v1)*v2_f)
REVERSE_J_LIBRARY1[np.power]            =lambda v3,v3_r,v1,v1_r,v2,v2_r:"    %s+=%s*%s*%s/%s \n    %s+=%s*log(%s)*%s"  %(v1_r,v3_r,v2,v3,v1,v2_r,v3_r,v1,v3)

#if va[1] not a adfloat
#-- v2_f = 0
REVERSE_J_LIBRARY2 = {}

#v3_f = v1_f - v2_f
REVERSE_J_LIBRARY2[np.subtract]         =lambda v3,v3_r,v1,v1_r,v2:"    %s+=%s"        %(v1_r,v3_r)
REVERSE_J_LIBRARY2[np.float.__rsub__]   =lambda v3,v3_r,v1,v1_r,v2:"    %s+=-%s"       %(v1_r,v1_r)
#v3_f = v1_f + v2_f
REVERSE_J_LIBRARY2[np.add]              =lambda v3,v3_r,v1,v1_r,v2:"    %s+=%s"        %(v1_r,v3_r)
#v3_f = v1_f*v2 + v2_f*v1
REVERSE_J_LIBRARY2[np.multiply]         =lambda v3,v3_r,v1,v1_r,v2:"    %s+=%s*%s"      %(v1_r,v3_r,v2)
#v3_f = (v1_f + v3*v2_f)/v2
REVERSE_J_LIBRARY2[np.divide]           =lambda v3,v3_r,v1,v1_r,v2:"    %s+=%s/%s"       %(v1_r,v3_r,v2)
REVERSE_J_LIBRARY2[np.float.__rdiv__]   =lambda v3,v3_r,v1,v1_r,v2:"    %s+=-%s*%s/%s"   %(v1_r,v3_r,v3,v1)
#v3_f = -sin(v1)*v1_f
REVERSE_J_LIBRARY2[np.cos]              =lambda v3,v3_r,v1,v1_r,v2:"    %s+=-sin(%s)*%s"  %(v1_r,v1,v3_r)
#v3_f = cos(v1)*vf_1
REVERSE_J_LIBRARY2[np.sin]              =lambda v3,v3_r,v1,v1_r,v2:"    %s+=cos(%s)*%s"   %(v1_r,v1,v3_r)
#v3_f = (1 + v3**2)*v1_f
REVERSE_J_LIBRARY2[np.tan]              =lambda v3,v3_r,v1,v1_r,v2:"    %s+=(1.0+%s**2)*%s" %(v1_r,v3,v3_r)
#v3_f = v3 * (v1_f/v1 * v2 + ln(v1)*v2_f)
REVERSE_J_LIBRARY2[np.power]            =lambda v3,v3_r,v1,v1_r,v2:"    %s+=%s*%s/%s*%s" %(v1_r,v3,v3_r,v1,v2)
#v3_f = exp(v1)*v1_f
REVERSE_J_LIBRARY2[np.exp]              =lambda v3,v3_r,v1,v1_r,v2:"    %s+=exp(%s)*%s"   %(v1_r,v1,v3_r)
#v3_f = 1/sqrt(1-x**2)
REVERSE_J_LIBRARY2[np.arcsin]           =lambda v3,v3_r,v1,v1_r,v2:"    %s+=1.0/(sqrt(1-%s**2))*%s"   %(v1_r,v1,v3_r)
#v3_f = -1/sqrt(1-x**2)
REVERSE_J_LIBRARY2[np.arccos]           =lambda v3,v3_r,v1,v1_r,v2:"    %s+=-1.0/(sqrt(1-%s**2))*%s"   %(v1_r,v1,v3_r)
#v3_f = 1/(v1**2+1)
REVERSE_J_LIBRARY2[np.arctan]           =lambda v3,v3_r,v1,v1_r,v2:"    %s+=1.0/(%s**2+1)*%s"   %(v1_r,v1,v3_r)
#v3_f = 1/(2*v3)
REVERSE_J_LIBRARY2[np.sqrt]             =lambda v3,v3_r,v1,v1_r,v2:"    %s+=1.0/(2*%s)*%s"   %(v1_r,v3,v3_r)
#v3_f = 1/(v1)*v1_f
REVERSE_J_LIBRARY2[np.log]              =lambda v3,v3_r,v1,v1_r,v2:"    %s+=1.0/(%s)*%s"   %(v1_r,v1,v3_r)
#v3_f = 1/(v1 * log(10)*v1_f
REVERSE_J_LIBRARY2[np.log10]            =lambda v3,v3_r,v1,v1_r,v2:"    %s+=1.0/(%s*log(10))*%s"   %(v1_r,v1,v3_r)
#v3_f = -v1_f
REVERSE_J_LIBRARY2[np.negative]         =lambda v3,v3_r,v1,v1_r,v2:"    %s+=-%s"   %(v1_r,v3_r)
REVERSE_J_LIBRARY2[np.float.__rpow__]   =lambda v3,v3_r,v1,v1_r,v2:"    %s+=%s*log(%s)*%s"  %(v1_r,v3_r,v2,v3)
