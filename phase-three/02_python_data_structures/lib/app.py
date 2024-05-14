# Sequence Types
# docs: 
# https://docs.python.org/3/tutorial/datastructures.html
import ipdb

#lists, tuples, dictionaries, and sets are all individual data types that are used to store collections of data.  they each have their own unique properties/behaviors.  a lot of those behaviors overlap

# Creating Lists
#✅ 1. Create a list of 10 pet names
pets=['Looney', 'Daisy', 'Kami', 'Bruno', 'Maya', 'Bailey', 'Bachman', 'Apollo', 'Tobi']

#------------------------ Reading Information from Lists
#✅ 1a. Return the first pet name 
pets[0]

#✅ 1b. Return the last value
pets[7]
#same as:
# pets[len(pets)-1]
# pets[-1]

#✅ 1c. Return all pet names beginning from the 3rd index
pets[3:]

#✅ 1d. Return all pet names before the 3rd index

pets[0:3]
#same as
# pets[:3]

#✅ 1e. Return all pet names beginning from the 3rd index and up to (exclusive of) the 7th
pets[3:7]

#✅ 1f. Find the index of a given element
pets.index('Daisy')
# if there are duplicates, it will only give you the first index

#✅ 1g. Reverse the original list
# mutate our list, destructive
# does not return anything

pets.reverse()


#✅ 1h. Return the frequency of a given element 
pets.count('Daisy')

#---------------------------------- Updating Lists
#✅ 1i. Change the first element to all uppercase
pets[0]=pets[0].upper()
pets[0]=pets[0].lower()

#---------------------------------- Adding items to list
#✅ 1j. Append a new name to the list
pets.append('Mushu')

#✅ 1k. Add a new name at a specific index
pets.insert(2,'Gunner')

#✅ 1l. Add two lists together 
new_names=['Althea', 'Avery']
combined_list = new_names + pets

#---------------------------------- Removing 
#✅ 1m. Removes and returns the final element from the list
pets.pop()
 
#✅ 1n. Remove element by specific index
pets.pop(5)

#✅ 1o. Remove a the first instance of a specific element 
pets.remove('Avery')

#✅ 1p. Remove all pet names from the list
pets.clear()
#---------------------------------- Tuple 
# can't mutate tuples
# can have repeats
#🛑 Using a trailing comma for a singleton tuple: a, or (a,)
#✅ 2. Create a Tuple of pet 10 ages 
# if only one element in the tuple, you MUST include the trailing comma!!!!!
# cant be mutated!

ages = (1,10,5,3,5,8,2,0)


#✅ 2a. Print the first pet age
print(ages[0])

#---------------------------------- Testing Changeability 
#✅ 2b. Attempt to remove an element with .pop (should error)
ages.pop('5')

#✅ 2c. Attempt to change the first element (should error)
ages[0]= 100

#---------------------------------- Tuple Methods
#✅ 2d. Return the frequency of a given element
ages.count(5)

#✅ 2e. Return the index of first matching element 
ages.index(5)

#---------------------------------- Demo Sets
#✅ 3. Create a set of 3 pet foods
pet_foods={'Blue Buffalo', 'Purina', 'Costco'}

# Demo Dictionaries 
#---------------------------------- Creating 
#✅ 4. Create a dictionary of pet information with the keys name, age and breed
# KEYS AS STRINGS
pet = {
    'name': 'Rose',
    'age': 11,
    'type': 'Cat'
    }

#✅ 4a.  Use dict to create a dictionary of pet information with the keys name, age and breed

other_cat=dict(name='Rose', age='10', type='Cat')

#---------------------------------- Reading
#✅ 4b. Print the pet attribute of name using bracket notation
pet['name']

#✅ 4c. Print the pet attribute of age using .get
pet.get('name')

#---------------------------------- Updating 
#✅ 4d. Update the pets age to 12

pet['age'] = 12

#✅ 4e. Update the other pets age to 26
other_cat.update(age = 28)
#same as
# pet.update({'age': 26})

#---------------------------------- Deleting
#✅ 4f. Delete a pets age using the del keyword 
del pet['age']

#✅ 4g. Delete the other pets age using the .pop, returns removed value
other_cat.pop('age')

#✅ 4h. Delete the last item in the pet dictionary using popitem()

pet.popitem()
# pops the last added key value pair and prints it

#✅ 5. loop through a range of 10 and print every number within the range

list(range(50,60,2))
#  will print as [50, 52, 54, 56, 58]

for num in range(10):
    print(num)
    # will print 
    # 50
    # 52
    # 54
    # 56
    # 58

#✅ 5a. loop through a range between 50 and 60 that iterates by 2 and print every number
#range(start, stop, increment)
for num in range(50,60,2):
    print(num)


#✅ 5b. Loop through the pet_info list and print every dictionary  

pet_info = [
    {
        'name': 'Rose',
        'age': 10,
        'type': 'Cat',
    },
    {
        'name': 'Apollo',
        'age':2,
        'type': 'dog',
    },
     {
        'name': 'Daisy',
        'age':4,
        'type': 'dog',
    }
]
for pet in pet_info:
    print(pet['name'])

#✅ 6. Create a function that takes a list as an argument. 
 
def print_list(lst):
    print(lst)
    
print_list(pet_info)

#✅ 7. Create a function that takes a list as an argument.(simple example) 



#✅ 8. Create a function that updates the age of a given pet
#replace_age(pet_info, "spot", 2) # => { 'name': "spot", 'age': 2, 'breed': "boxer"}
#replace_age(pet_info, "does_not_exist", 5) # => 'pet not found'

def replace_age(pet_list, name, new_age):
    found = False
    for pet in pet_list:
        if pet['name']==name:
            found = True
            pet['age']=new_age
            break
        
        if not found:
            print('Pet not found!')
            
    replace_age(pet_info, 'Apollo', 3)
# map like 
#✅ 9. Use list comprehension to return a list containing every pet name from pet_info changed to uppercase
[pet ['name'] for pet in pet_info]


# find like
#✅ 9a. Use list comprehension to find a pet named spot
[pet['name':'spot'] for pet in pet_info]


# filter like
#✅ 9b. Use list comprehension to find all of the pets under 3 years old
older_pets = [pet for pet in pet_info if pet['age'] >3]
young_pets = [pet for pet in pet_info if pet['age'] <3]