def walk(pet_name):
    print(f'{pet_name} has been for a walk')
    
def feed(pet_name):
    print(f'{pet_name} has been feed')
    
    # higher order function: function parameter and/or return functions
    
def execute_function(func, name):
    func(name)
    
import ipdb; ipdb.set_trace