from math import pi

factorial = (lambda f: (lambda x: 1 if x==0 or x==1 else x * f(f, x-1))) (lambda f, x: 1 if x==0 or x==1 else x *f(f, x-1))


sine_x = (lambda s: lambda  x, n: sum(((-1 ** k) * ((x * (pi / 180)) ** (2* k + 1)) / factorial(2 * k + 1) for k in range(n))))

result=0
recursivesum = (lambda f: (lambda n: None if n<=0 else (globals().__setitem__('result' ,result + n ), f(f, n-1))[1])) (lambda f, n: None if n<=0 else (globals().__setitem__('result' ,result + n ), f(f, n-1))[1])


