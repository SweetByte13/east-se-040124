from flask import request, make_response, session
from config import app, db, api
from models import Project, User
from flask_restful import Resource

import ipdb

class Projects(Resource):
    def get(self):
        projects = Project.query.all()
        projects_list = [project.to_dict() for project in projects]
        return make_response(projects_list)

    def post(self):
        data = request.json
        try:
            project = Project(name=data['name'],\
                             about=data['about'],\
                             phase=data['phase'],\
                             link=data['link'],\
                             image=data['image']\
                            )
            db.session.add(project)
            db.session.commit()
            return make_response(project.to_dict(), 201)
        except:
            return make_response({'error': "couldn't create project"}, 400)


api.add_resource(Projects, '/projects')

class ProjectById(Resource):
    def get(self, id):
        project = Project.query.get(id)
        return make_response(project.to_dict())

api.add_resource(ProjectById, '/projects/<int:id>')


# 3a. define /signup route
class SignUp(Resource):
    def post(self):
        params = request.json
        try:
            user = User(username=params.get('username'))
            user.password_hash = params.get('password')
            db.session.add(user)
            db.session.commit()
            session['user_id'] = user.id
            return make_response(user.to_dict(), 201)
        except Exception as e:
            return make_response({"error": "Something went wrong"}, 400)
    
api.add_resource(SignUp, '/signup')

# 4a. create /check_session route
    # b. request from frontend
    # c. check for user_id in session
    # d. if user_id, find user send back response
    # e. else send back error response
class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if user_id:
            user = db.session.get(User, user_id)
            if user:
                return make_response(user.to_dict(), 200)
        return make_response({"error": "Unauthorized: Must login"}, 401)
        
api.add_resource(CheckSession, '/check_session')

# 5. create /logout route
    #  remove user_id from session
class Logout(Resource):
    def delete(self):
        session['user_id'] = None
        return make_response({}, 204)
    
api.add_resource(Logout, '/logout')

# 6a. create /login route
class Login(Resource):
    def post(self):
        params = request.json
        user = User.query.filter_by(username=params.get('username')).first()
        if user.authenticate(params.get('password')):
            session['user_id'] = user.id
            return make_response(user.to_dic())
        else:
            return make_response({"error": 'invalid password'}, 401)
            
api.add_resource(Login, '/login')
# 6c. add user_id to session