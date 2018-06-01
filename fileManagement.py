'''
Restricting Globals
For this reason, you may want to control what gets unpickled by customizing Unpickler.find_class().
Unlike its name suggests, Unpickler.find_class() is called whenever a global (i.e., a class or a function) is requested.
Thus it is possible to either completely forbid globals or restrict them to a safe subset.
Here is an example of an unpickler allowing only few safe classes from the builtins module to be loaded:
'''
import builtins
import io
import pickle

safe_builtins = {
    'range',
    'complex',
    'set',
    'frozenset',
    'slice',
}

class RestrictedUnpickler(pickle.Unpickler):

    def find_class(self, module, name):
        # Only allow safe classes from builtins.
        if module == "builtins" and name in safe_builtins:
            return getattr(builtins, name)
        # Forbid everything else.
        else:
            print("global '%s.%s' is forbidden" %(module, name))
            raise pickle.UnpicklingError("global '%s.%s' is forbidden" %(module, name))

def restricted_loads(s):
    """Helper function analogous to pickle.loads()."""
    return RestrictedUnpickler(io.BytesIO(s)).load()

print(restricted_loads(pickle.dumps([1, 2, range(15)])))
#print(restricted_loads(b"cos\nsystem\n(S'echo hello world'\ntR."))




'''
Handling Stateful Objects
Here’s an example that shows how to modify pickling behavior for a class.
The TextReader class opens a text file, and returns the line number and line contents each time its readline() method is called.
If a TextReader instance is pickled, all attributes except the file object member are saved.
When the instance is unpickled, the file is reopened, and reading resumes from the last location.
The __setstate__() and __getstate__() methods are used to implement this behavior.
'''
import json
class Person:
    def __init__(self, name, mobile, email, creditcard="0000000000000"):
        self.name, self.mobile, self.email = name, mobile, email
        self.__creditcard = creditcard
    def describe(self):
        print("Name - " + self.name)
        print("Mobile - " + self.mobile)
        print("Email - " + self.email)
    def __getstate__(self):
        #print("__getstate__() called.")
        state = self.__dict__.copy()
        return state
    def __setstate__(self, state):
        #print("__setstate__() called.")
        self.__dict__.update(state)

person1 = Person("Adam", "9066191461", "hellotathagat@gmail.com", "32342342342")
person1.name = "Tathagat"

person1.describe()
print(json.dumps(person1, default=lambda o: o.__dict__))
print("Saving pickle.")
with open('data.pickle', 'wb') as f:
    # Pickle the 'data' dictionary using the highest protocol available.
    pickle.dump(person1, f, pickle.HIGHEST_PROTOCOL)
print("Loading pickle.")
with open('data.pickle', 'rb') as f:
    person2 = pickle.load(f)
    person2.describe()




'''
Using the shelve module to persist data dictionary
'''
import shelve
myshelve = shelve.open('data.shelve', writeback=True)
myshelve['person1'] = person1
myshelve['person2'] = Person("Eve", "8766283838", "eve@gmail.com")
myshelve['countries'] = {'developed':['USA','UK','JAPAN'], 'developing':['INDIA', 'CHINA']}
print(myshelve)
for keys in myshelve:
    print(myshelve[keys])
myshelve.close()
myshelve1 = shelve.open('data.shelve', writeback=True)
myshelve1['person1'] = "DELETED"
myshelve1.close()
myshelve2 = shelve.open('data.shelve', writeback=True)
for keys in myshelve2:
    print(myshelve2[keys])
myshelve2.close()


