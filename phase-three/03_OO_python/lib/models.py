#!/usr/bin/env python3
import ipdb; 

"""
Pet
    - name
    - age
    - breed
"""
#✅ 1. Create a Pet class
#PASCAL CASING - first letter of each word is capitilized
class Pet:
    def __init__(self, name="Pet", age=0, breed='Unknown'):
        self.name = name
        self.age = age
        self.breed = breed
        
    def speak(self):
        if self.breed == 'Dog':
            print('Bark')
        elif self.breed == 'Cat':
            print('Meow')
        else:
            print('...silence')

    def __repr__(self):
        return f'<Pet={self.name}>'

    #✅ 3. Demonstrate __init__
    #✅ 3a. Add parameters for attributes
    #✅ 3b. use dot notation to access their attributes
    #✅ 3c. update attributes with new values

    #✅ 4. Demonstrate INSTANCE methods
    #✅ 4a. Create a hello method that will print "Hello!"
    #✅ 4b. Create a print_pet_details function that will print the pet attributes
    #✅ 4c. Create a speak method that will print "Woof" for dogs and "Meow" for cats


#✅ 5. Set constraints for updating properties (attributes that are controlled by methods)
    #✅ 5a. Create Owner class
class Owner:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #✅ 5b. Create get/set instance methods for name property
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if type(new_name) == str:
            self._name=new_name
        else:
            raise TypeError('Name must be of type str')
        
    name = property(get_name, set_name)
    
    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise TypeError ('Age must be an integer')
        
    age = property(get_age, set_age)
    #✅ 5c. Create constraint to make sure the name is of type string
    #✅ 5d. Compile get_name, set_name under the same property name (@ decorator is syntactic sugar)
    #✅ 5e. Add parameter to pass in name property value on instantiation
    #✅ 5f. Use the name property to set the name "private" attribute on instantiation
ipdb.set_trace()
