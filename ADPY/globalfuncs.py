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

import math
import numpy

import string
#import utils

# override numpy definitions
numpy_function_names = [
        'exp', 'log', 'log10', 'sqrt', 'pow',
        'sin', 'cos', 'tan',
        'arcsin', 'arccos', 'arctan',
        'sinh', 'cosh', 'tanh',
        'sign']


function_template = string.Template('''
def $function_name(*args, **kwargs):
    """
    generic implementation of $function_name

    this function calls, depending on the input arguments,
    either

    * numpy.$function_name
    * numpy.linalg.$function_name
    * args[i].__class__

    """
    case,arg = 0,0
    for na,a in enumerate(args):
        if hasattr(a.__class__, '$function_name'):
            case = 1
            arg  = na
            break

    if case==1:
        return getattr(args[arg].__class__, '$function_name')(*args, **kwargs)

    elif case==0:
        return $namespace.__getattribute__('$function_name')(*args, **kwargs)

    else:
        return $namespace.__getattribute__('$function_name')(*args, **kwargs)
''')

for function_name in numpy_function_names:
    exec function_template.substitute(function_name=function_name,
                                      namespace='numpy')

