"""
Wishlist model for tracking bottles users want to purchase.

Represents wishlist items in the MyCask application, tracking bottles users
want to purchase with optional target prices and price drop notifications.
"""

from ..db.database import Base
from sqlalchemy import Column, Integer, DateTime, Decimal, Boolean, ForeignKey, func
from sqlalchemy.orm import relationship
from .user import User
from .bottle import Bottle

class Wishlist(Base):
    __tablename__ = "wishlists"

    id = Column(Integer, index=True, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    bottle_id = Column(Integer, ForeignKey(Bottle.id, ondelete="CASCADE"), nullable=False)
    target_price = Column(Decimal(precision=10, scale=2), nullable=True)
    notify_on_drop = Column(Boolean, default=False, nullable=False)
    added_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="wishlists")
    bottle = relationship("Bottle", back_populates="wishlists")
