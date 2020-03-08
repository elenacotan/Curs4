'''	A(x) = |x| * x^3;
	B(x) = lg⁡x + ln⁡x;
	C(x) = sin(x) + six(x) * cos(x);
	D(x) = e^x + 2 * arctg(x) – x;
'''
import math

def A(x):
    return abs(x) * x**3

def B(x):
    return math.log(x,10) + math.log1p(x)

def C(x):
    return math.sin(x) + math.sin(x)*math.cos(x)

def D(x):
    return math.exp(x) + 2 * math.atan(x) - x 

x = int(input("Introduceti un numar intreg x: "))
print(A(x))
print(B(x))
print(C(x))
print(D(x))
