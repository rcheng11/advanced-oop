class Dog:
    '''
    The Dog class represents a dog object that can store a list of treats.
    '''
    def __init__(self, name):
        '''
        Initializes the function with a name and creates a treats dict
        '''
        self.name = name
        self.treats = {}
        self.max = 1
    def speak_treat(self, treat):
        '''
        Prints out the treat it's speaking
        '''
        print("I ate your " + str(treat))
    def say_grace(self):
        '''
        The dog will now say grace for all the treats he's eaten.
        '''
        for index in self.treats:
            self.speak_treat(self.treats[index])
        print("Thanks for supporting my lifestyle!")
    # "magic methods" are methods with double underscores surrounding them
    # __init__ is also a "magic method"
    def append(self, treat):
        self.__setitem__(self.max - 1, treat)
        self.max += 1
    def __getitem__(self, key):
        return self.treats[key]
    def __setitem__(self, key, value):
        if(type(key) == type(1)):
            self.treats[key] = value
        else:
            print("Error: Bad index.")
    def __eq__(self, other):
        return self.name == other.name
    def __int__(self):
        return len(self.treats)
    def __str__(self):
        return "The dog " + self.name + " who has eaten " + str(len(self.treats)) + " treats"
class Treat:
    '''
    A Treat object that takes in a name (str) and a price (int)
    '''
    # again... magic methods
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __str__(self):
        return self.name + " which costs " + str(self.price) + " dollars!"