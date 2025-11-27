"""
Bottle model for TODO: description.

Represents general bottles in the MyCask application with various attributes.
"""

from ..db.database import Base
from sqlalchemy import Column, Integer, String, DateTime, Decimal, func

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
    image_url = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)