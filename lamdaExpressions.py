#lamda argument_list : expression
sum = lambda x, y : x + y
print(sum(3,4))




#map(func, seq)
def farenheit(T):
	return ((float(9)/5)*T + 32)
def celsius(T):
	return (float(5)/9) * (T-32)
tempretures = (0,20,40,60,80,100,120)
F = map(farenheit, tempretures)
C = map(celsius, tempretures)
print(tempretures)
print(list(F))
print(list(C))




#map and lambda
F_lambda = map(lambda T: ((float(9)/5)*T + 32), tempretures)
C_lamda = map(lambda T: (float(5)/9) * (T-32), tempretures)
print(list(F_lambda))
print(list(C_lamda))




#map and lamda with multiple lists(with same number of elements)
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
d = lambda x,y,z:(x+y+z), a,b,c
e = map(lambda x,y,z:(x+y+z), a,b,c)
print(e)
print(d)
print(list(e))
print(list(d))



#Mapping of functions
from math import sin, cos, tan, pi
def map_functions(x, functions):
	return [func(x) for func in functions]

family_of_functions = (sin, cos, tan)
print(map_functions(30, family_of_functions))




#Filtering
def greater_than(x,m):
	if x > m:
		return True
	else:
		return False

numbers = [1,2,3,4,5,6,7,8,9,10,11,12]
print(list(filter(lambda x: x%2, numbers)))
print(list(filter(lambda x: greater_than(x,5), numbers)))




#Reduce 
import functools
result = functools.reduce(lambda x,y: x+y, [1,2,3,4])
print(result)
greatest = lambda x,y: x if (x > y) else y
result = functools.reduce(greatest, numbers)
print(result) 



#initializing a lambda 
def intitialize_increment(n):
	return lambda x: x+n
s = intitialize_increment(33)
print(s)
print(s(3))
print(s(4))