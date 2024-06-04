from config import app
from flask import make_response
from models.dog import Dog

# REST convention
# GET all'/dogs'
# GET one '/dogs<int:id>'
# POST '/dogs'
# PATCH '/dogs<int:id>'
# DELETE '/dogs<int:id>'



@app.route('/dogs', methods=['GET'])
def get_all_dogs():
    all_dogs=[]
    for dog in Dog.query.all():
        # dog_dict={
        #     'id': dog.id,
        #     'name': dog.name,
        #     'age':dog.age,
        #     'favorite_treat': dog.favorite_treat
        # }
        all_dogs.append(dog.to_dict())
    return make_response(all_dogs)