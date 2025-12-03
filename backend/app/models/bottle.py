"""
Bottle model for the MyCask application.

Represents general bottles with various attributes. Supports both base bottles
and variants (e.g., single barrel picks, special releases) through a
self-referential relationship.
"""

from ..db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Numeric, Boolean, Date, ForeignKey, func
from sqlalchemy.orm import relationship

class Bottle(Base):
    __tablename__ = "bottles"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(200), nullable=False)
    distillery = Column(String(200), nullable=True)
    type = Column(String(50), nullable=True)  # e.g., bourbon, scotch, rye
    region = Column(String(100), nullable=True)
    age_years = Column(Integer, nullable=True)
    abv = Column(Numeric(precision=4, scale=2), nullable=True)  # e.g., "43.50"
    msrp = Column(Numeric(precision=10, scale=2), nullable=True)
    barcode = Column(String(50), unique=True, index=True, nullable=True)  # UK barcode
    description = Column(String, nullable=True)
    mashbill_description = Column(String(500), nullable=True)
    image_url = Column(String, nullable=True)
    
    # Base bottle vs variant
    is_variant = Column(Boolean, default=False, nullable=False)
    parent_bottle_id = Column(Integer, ForeignKey("bottles.id"), nullable=True)
    
    # Variant-specific fields
    barrel_number = Column(String(100), nullable=True)  # e.g., "Barrel 5-2B"
    warehouse = Column(String(50), nullable=True)  # e.g., "Warehouse K"
    batch_number = Column(String(100), nullable=True)  # e.g., "Batch B523"
    vintage_year = Column(Integer, nullable=True)  # For wines, whiskies with specific years
    proof_actual = Column(Numeric(precision=5, scale=2), nullable=True)  # Actual proof (may differ from standard)
    age_statement_actual = Column(String(50), nullable=True)  # e.g., "13 years 2 months"
    pick_information = Column(String, nullable=True)  # e.g., "Selected by Total Wine"
    tier_run = Column(String(50), nullable=True)  # e.g., "Tier 1" or "Run 2"
    bottle_date = Column(Date, nullable=True)  # When bottled
    release_info = Column(String, nullable=True)  # Any special release info
    
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    user_bottles = relationship("UserBottle", back_populates="bottle", cascade="all, delete-orphan")
    tastings = relationship("Tasting", back_populates="bottle", cascade="all, delete-orphan")
    bottle_prices = relationship("BottlePrice", back_populates="bottle", cascade="all, delete-orphan")
    wishlists = relationship("Wishlist", back_populates="bottle", cascade="all, delete-orphan")
    
    # Self-referential relationship for variants
    parent_bottle = relationship("Bottle", remote_side=[id], backref="variants")