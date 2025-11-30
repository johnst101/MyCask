"""
BottlePrice model for tracking bottle prices from various sources.

Represents price records for bottles in the MyCask application, tracking
prices from retailers or market sources over time.
"""

from ..db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Numeric, ForeignKey, func
from sqlalchemy.orm import relationship
from .bottle import Bottle

class BottlePrice(Base):
    __tablename__ = "bottle_prices"

    id = Column(Integer, index=True, primary_key=True)
    bottle_id = Column(Integer, ForeignKey(Bottle.id, ondelete="CASCADE"), nullable=False)
    price = Column(Numeric(precision=10, scale=2), nullable=True)
    source = Column(String(100), nullable=True)  # retailer or 'market'
    recorded_at = Column(DateTime, server_default=func.now(), nullable=False)

    # Relationships
    bottle = relationship("Bottle", back_populates="bottle_prices")

