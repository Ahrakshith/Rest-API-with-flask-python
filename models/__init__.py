# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import the association table
from models.user import UserModel
from models.item import ItemModel
from models.tag import TagModel
from models.store import StoreModel
from models.item_tags import ItemsTags