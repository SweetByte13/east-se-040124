class Pet:
    # total_count = 0
    all = []
    
    def __init__(self, name="Pet", age=0, breed='Unknown'):
        self.name = name
        self.age = age
        self.breed = breed
        
        # Pet.increase_pets()
        Pet.add_new_pet(self)
        
    # @classmethod
    # def increase_pets(cls):
    #     cls.total_count += 1
        
    @classmethod
    def add_new_pet(cls, new_pet):
        cls.all.append(new_pet)
        
    @classmethod
    def total_count(cls):
        return len(cls.all)

    def hello(self):
        print('Hello')

    def speak(self):
        if self.breed == 'Dog':
            print('Bark')
        elif self.breed == 'Cat':
            print('Meow')
        else:
            print('...silence')

    def __repr__(self):
        return f'<Pet name={self.name}>'