from flask_sqlalchemy import SQLAlchemy
from ..models import Model

db = SQLAlchemy(model_class=Model)