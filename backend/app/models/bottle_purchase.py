"""
BottlePurchase model for tracking purchase history of user bottles.

Represents purchase records for user bottles in the MyCask application,
tracking quantity, price, date, location, and notes for each purchase.
"""

from ..db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Date, Numeric, ForeignKey, func
from sqlalchemy.orm import relationship
from .user_bottle import UserBottle

class BottlePurchase(Base):
    __tablename__ = "bottle_purchases"

    id = Column(Integer, index=True, primary_key=True)
    user_bottle_id = Column(Integer, ForeignKey(UserBottle.id, ondelete="CASCADE"), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)
    purchase_price = Column(Numeric(precision=10, scale=2), nullable=True)
    purchase_date = Column(Date, nullable=True)
    purchase_location = Column(String(255), nullable=True)
    notes = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    user_bottle = relationship("UserBottle", back_populates="bottle_purchases")

