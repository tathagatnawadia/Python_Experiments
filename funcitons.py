#Remembers list,instances of classes and dictionaries
def f(a, L=[]):
	L.append(a)
	return L
def g(a,s="writing"):
	if a == "replace":
		s = a
	return s
print(f(1))
print(f(2))
print(f(3))
print(g(1))
print(g("replace"))
print(g(3))




#Not remember list,instances of classes and dictionaries
def f(a,L=None):
  if L is None:
    L = []
  L.append(a)
  return L
print(f(1))
print(f(2))
print(f(3,f(1)))



#*args and **kwargs
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")




#using dictionary as input to a function
def parrot(voltage, state='defaultState', action='defaultAction'):
	print("voltage=",voltage,end=' ')
	print("state=",state,end=' ')
	print("action=",action)
d = {'voltage':12.33, 'action':'flyfly'}
parrot(**d)




#constraing data types and using __annotations__
def f(arg1:str, arg2:str = 'defaultArg2') -> str:
	print("Annotations", f.__annotations__)
	return arg1+' '+arg2
print(f("hello"))