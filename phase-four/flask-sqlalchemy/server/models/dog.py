from config import db


class Dog(db.Model):
    __tablename___='dogs'
    
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    favorite_treat = db.Column(db.String)
    
def to_dict(self):
    return {
        'id': self.id,
        'name': self.name,
        'age':self.age,
        'favorite_treat':self.favorite_treat
    }