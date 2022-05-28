from flask import Flask
from .config import config
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask main app
app = Flask(__name__)
# Loading Flask configuration file
app.config.from_object(config)

# Create SQL ORM SQLAlchemy
db = SQLAlchemy(app)

# model import
from .model import User

# controller blueprint import
from .controller.admin import admin_blueprint
from .controller.main import main_blueprint











# Register blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(admin_blueprint, url_prefix = '/admin')

