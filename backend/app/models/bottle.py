"""
Bottle model for TODO: description.

Represents general bottles in the MyCask application with various attributes.
"""

from ..db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Decimal, func
from sqlalchemy.orm import relationship

class Bottle(Base):
    __tablename__ = "bottles"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(200), nullable=False)
    distillery = Column(String(200), nullable=True)
    type = Column(String(50), nullable=True)  # e.g., bourbon, scotch, rye
    region = Column(String(100), nullable=True)
    age_years = Column(Integer, nullable=True)
    abv = Column(Decimal(precision=4, scale=2), nullable=True)  # e.g., "43.50"
    msrp = Column(Decimal(precision=10, scale=2), nullable=True)
    barcode = Column(String(50), unique=True, index=True, nullable=True)  # UK barcode
    description = Column(String, nullable=True)
    mashbill_description = Column(String(500), nullable=True)
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    user_bottles = relationship("UserBottle", back_populates="bottle", cascade="all, delete-orphan")
    tastings = relationship("Tasting", back_populates="bottle", cascade="all, delete-orphan")
    bottle_prices = relationship("BottlePrice", back_populates="bottle", cascade="all, delete-orphan")
    wishlists = relationship("Wishlist", back_populates="bottle", cascade="all, delete-orphan")