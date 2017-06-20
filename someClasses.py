from copy import copy,deepcopy


class Person(object):
    __instances = 0;

    def __init__(self, name="", email="", country=""):
        Person.__instances += 1
        self.__setattr__('name', name)
        self.__setattr__('email', email)
        self.__setattr__('country', country)

    def __del__(self):
        Person.__instances -= 1

    @staticmethod
    def hello():
        print("Hello I have ", Person.__instances, " people.")

    def __copy__(self):
        return type(self)(country=self.country)

    def __deepcopy__(self, memodict={}):
        return type(self)(deepcopy(self, memodict))

Person.hello()
a = Person("One", "one@aon.com", "germany")
b = Person("Two", "two@aon.com", "france")
print(b.name)
c = copy(b)
print(c.__dict__)
Person.hello()
del a
Person.hello()


class Record(dict):
    def __init__(self, *args, **kwargs):
        super(Record, self).__init__(*args, **kwargs)
        self.__dict__ = self

    def __str__(self):
        items = ["%r: %r" % (k, v) for k, v in sorted(self.__dict__.items())]
        return "{" + ", ".join(items) + "}"

    def __copy__(self):
        return Record(**self.__dict__.copy())

    def __deepcopy__(self, memo):
        address = id(self)
        try:
            return memo[address]
        except KeyError:
            memo[address] = {k: copy(v) for k, v in self.items()}
            return deepcopy(self, memo)


def someFunction(x=None):
    if x is None:
        return 1
    return x+1

L = range(5)
one = Record(x=1, y=2, s=[1,2,3], t={"name": [33,44,99]}, a=L, b=someFunction)
two = copy(one)
three = deepcopy(one)
print(one)
print(two)
print(three)
L.insert(33,55)
print(one)
print(two)
print(three)