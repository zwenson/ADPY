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

