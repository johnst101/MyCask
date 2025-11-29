"""
UserBottle model for specific bottles owned by users.

Represents bottles owned by users in the MyCask application with an id and mutltiple FKs.
"""

from ..db.database import Base
from sqlalchemy import Column, Integer, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship

class UserBottle(Base):
    __tablename__ = "user_bottles"

    id = Column(Integer, index=True, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)  # FK to users.id "ON DELETE CASCADE"
    bottle_id = Column(Integer, ForeignKey("bottles.id", ondelete="CASCADE"), nullable=False)  # FK to bottles.id "ON DELETE CASCADE"
    current_quantity = Column(Integer, default=0)
    added_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="user_bottles")
    bottle = relationship("Bottle", back_populates="user_bottles")
    bottle_purchases = relationship("BottlePurchase", back_populates="user_bottle", cascade="all, delete-orphan")
