"""
UserBottle model for specific bottles owned by users.

Represents bottles owned by users in the MyCask application with an id and mutltiple FKs.
"""

from ..db.database import Base
from models.bottle import Bottle
from models.user import User
from sqlalchemy import Column, Integer, DateTime, func, ForeignKey

class UserBottle(Base):
    __tablename__ = "user_bottles"

    id = Column(Integer, index=True, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)  # FK to users.id "ON DELETE CASCADE"
    bottle_id = Column(Integer, ForeignKey(Bottle.id), nullable=False)  # FK to bottles.id "ON DELETE CASCADE"
    current_quantity = Column(Integer, default=0)
    added_at = Column(DateTime, server_default=func.now(), nullable=False)
