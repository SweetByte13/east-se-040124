from config import app, db
from models.dog import Dog


if __name__ == '__main__':
    with app.app_context():
       Dog.query.delete()
       db.session.commit()
       
       apollo=Dog(name='Apollo', age = 4, favorite_treat= 'chicken')
       daisy=Dog(name='Daisy', age = 2, favorite_treat= 'all food')
       bailey=Dog(name='Bailey', age = 13, favorite_treat= 'steak')
       
       db.session.add_all([apollo,daisy,bailey])
       db.session.commit()