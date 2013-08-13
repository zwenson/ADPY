ADPY
====

##Discription


ADPY is a Python library for algorithmic differentiation (http://en.wikipedia.org/wiki/Automatic_differentiation).
It aims to provide an easy way to extract partial derivatives of vector valued function. In addition it allows to created callable function for obtaining function values using computational graphs.  

Features:

* optimize numerical evaluation by using computational graph
* create callable function from Sympy expressions (calls lambdify once and creates a computational graph) 
* extract partial derivatives using forward or reverse algorithmic differentiation
* bonus: a small nonlinear solver using all advantages mentioned above



##How to use

Due the small amount of features the handling is quite easy. 
For the easiest use you need a callable function which takes a list of float numbers and returns a list.

    	def f(x):
        	return [x[0]**2,2*x[1]]

You need a valid values for x which cause no singularities while evaluating the function.

		x1 = [1.,2.]

Initialize the ADFUN object.

		from ADPY import adfun
		adpy_test  = adfun(f,x1)

Now you have a callable function with computational graph optimization.

			y1 = adpy_test(x1)

If you want to use derivatives just do
	
		adpy_test.init_reverse_jac()

or::

		adpy_test.init_forward_jac()

Now you can evaluate them using

		J_forward = adpy_test.jac_reverse(x1)

or::

		J_forward = adpy_test.jac_forward(x1)