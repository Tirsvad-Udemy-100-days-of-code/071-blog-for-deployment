"""! @file database.py
@brief The Flask-SQLAlchemy extension shared by the persistence models and the composition root.
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """! @brief Declarative base of all persistence models."""


## The one database extension; it is bound to an application in create_app.
db = SQLAlchemy(model_class=Base)
