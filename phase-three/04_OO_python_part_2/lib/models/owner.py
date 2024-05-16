#!/usr/bin/env python3
import ipdb; 
from models.person import Person

"""
SWABATs:
 - Create a new Python class
 - Pass new instances information during instantiation
 - Give our new class methods
 - Protect attributes with properties
"""



class Owner(Person):
    def __init__(self, name, age, experience=0):
        super().__init__(name, age)
        self.experience = experience

    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            raise TypeError('Name must be of type str')
    
    name = property(get_name, set_name)

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise TypeError('Age must be an integer')

    age = property(get_age, set_age)



# ipdb.set_trace()