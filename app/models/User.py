from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
import Model

class User(Model):
    id = mapped_column(Integer, primary_key=True)
    email = mapped_column(String(255), unique=True, nullable=False)
    password = mapped_column(String(255), nullable=False)
    fullname = mapped_column(String(255), nullable=False)
    surnames = mapped_column(String(255))
    contact = mapped_column(Integer, nullable=False)
    role = mapped_column(String, nullable=False)
    created_at = mapped_column(String, nullable=False)