"""
Tasting model for user tasting records.

Represents tasting records in the MyCask application, tracking user ratings,
notes, and dates for bottles they have tasted.
"""

from ..db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Date, ForeignKey, CheckConstraint, func
from sqlalchemy.orm import relationship
from .user import User
from .bottle import Bottle

class Tasting(Base):
    __tablename__ = "tastings"
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )

    id = Column(Integer, index=True, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)
    bottle_id = Column(Integer, ForeignKey(Bottle.id, ondelete="CASCADE"), nullable=False)
    rating = Column(Integer, nullable=False)  # CHECK 1-5
    notes = Column(String, nullable=True)
    tasting_date = Column(Date, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="tastings")
    bottle = relationship("Bottle", back_populates="tastings")
    tasting_flavors = relationship("TastingFlavor", back_populates="tasting", cascade="all, delete-orphan")

