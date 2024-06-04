from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'


db = SQLAlchemy()


migrate = Migrate(app, db)

db.init_app(app)

# flask db init -> initalized our migrate repo
# flask db migrate -m "detailed message of change" -> creates a new migration
#   compared whats in the models that are imported in app.py to what is in the database
#   migration will contain how t o update the db campared off what was changed
# flask db upgrade -> run the newest migration upgrade function
# flask db downgrade -> will downgrade the previous migration 