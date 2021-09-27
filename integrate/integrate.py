from sympy import Integral, Symbol

def func(function):
	x = Symbol('x')

	integral = Integral(function, x).doit()
	return function.evalf()


def integrate(function, minimum, maximum):
	x = Symbol('x')
	if minimum and maximum:
		return Integral(function, (x, minimum, maximum)).doit()
	else:
		return Integral(function, x).doit()
