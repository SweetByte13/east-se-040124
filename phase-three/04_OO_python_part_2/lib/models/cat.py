from models.pet import Pet

class Cat(Pet):
    def __init__(self, name="", age=0, breed="", indoor= True):
        super().__init__(name,age,breed)
        self.indoor = indoor
        
    def __repr__(self):
        return f'<Cat name={self.name} indoor={self.indoor}/>'