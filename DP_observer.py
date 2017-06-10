class GlobalWealth(object):
    def __init__(self):
        self._global_wealth = 10.0
        self._observers = []

    def get_wealth(self):
        return self._global_wealth

    def set_wealth(self, value):
        self._global_wealth = value
        for callback in self._observers:
            print('anouncing change')
            callback(self._global_wealth)

    '''
    property() can be used in case you made a variable from x to __x and and still want people to use it
    Good for backward compatibility.
    Eg. x = property(new_getter_for__x, new_setter_for__x)
    Therefore classname.x = 10, this will call new_setter_for__x(10) and set __x

    Alternatively we can use
    @property
    def temperature(self):
        print("Getting value")
        return self._temperature
    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value
    '''
    global_wealth = property(get_wealth, set_wealth)

    def bind_to(self, callback):
        print('bound')
        self._observers.append(callback)


class Person(object):
    def __init__(self, data):
        self.wealth = 1.0
        self.data = data
        self.data.bind_to(self.update_how_happy)
        self.happiness = self.wealth / self.data.global_wealth

    def update_how_happy(self, global_wealth):
        self.happiness = self.wealth / global_wealth


if __name__ == '__main__':
    data = GlobalWealth()
    p = Person(data)
    print(p.happiness)
    data.global_wealth = 1.0
    print(p.happiness)