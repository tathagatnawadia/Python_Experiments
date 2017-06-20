from util.utils import *
# A simple generator
cities = ["Paris", "Berlin", "Hamburg"]
for location in cities:
    print(location)


# Using "next" and "iter"
city_iterator = iter(cities)
while city_iterator:
    try:
        city = next(city_iterator)
        print(city, " ", end="")
    except Exception as e:
        print("Exception caught !! ", e.__class__)
        break


# Using yield()
def fibonacci():
    """Generates an infinite sequence of Fibonacci numbers on demand"""
    a, b = 0, 1
    while True:
        # Dont worry about unending while, since python saves state of local objects
        # once a yield statement is called.
        # Next time the function is called, python will continue with the while
        yield a
        a, b = b, a + b

f = fibonacci()

counter = 0
for x in f:
    print(x, " ", end="")
    counter += 1
    if counter > 5:
        break
print()


# Generator can have return statements too
def gen():
    yield 1
    yield 2
    return -1

try:
    g = gen()
    print(next(g), next(g), next(g))
except Exception as e:
    print("Exception caught !! ",e.__class__, e)


# Using "yield from"
def gen():
    yield from cities

g = gen()
for x in g:
    print(x, " ", end="")


# .send() to generators and wrapping them around
from functools import wraps
def get_ready(gen):
    """
    decorator to advance to first yield
    """
    @wraps(gen)
    def generator(*args, **kwargs):
        g = gen(*args, **kwargs)
        next(g)
        return g
    return generator


@get_ready
def infinite_looper(objects):
    # Setting up the infinite looper
    count = -1
    message = yield None
    while True:
        if message != None:
            # If no index(message) was given count = 0
            # else count = message
            count = 0 if message < 0 else message
        count += 1
        if count >= len(objects):
            # If overflow count = 0
            count = 0
        message = yield objects[count]

x = infinite_looper(["pacman", 1, {"name": "Nawadia"}, 3.3344, ("red", "green", "blue")])
print(next(x))
print(x.send(2))
print(next(x))
print(next(x))


# Using itertools with powerset, combinations and permutations
import itertools
combi = itertools.combinations(['red', 'green', 'blue'],2)
perms = itertools.permutations(['red', 'green', 'blue'])
print(list(combi))
print(list(perms))


# TODO : recursive generators

