ADPY
====

##Discription


ADPY is a Python library for algorithmic differentiation (http://en.wikipedia.org/wiki/Automatic_differentiation).
It aims to provide an easy way to extract partial derivatives of vector valued function. In addition it allows to created callable function for obtaining function values using computational graphs.  

* optimize numerical evaluation by using computational graph
* create callable function from Sympy expressions (calls lambdify once and creates a computational graph) 
* extract partial derivatives using forward or reverse algorithmic differentiation
* bonus: a small nonlinear solver using all advantages mentioned above


##How to use

Due the small amount of features the handling is quite easy. 
For the easiest use you need a callable function which takes a list of float numbers and return a list::
    $def f(x):
    $    return 