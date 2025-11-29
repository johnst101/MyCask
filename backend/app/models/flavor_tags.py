"""
FlavorTag model for categorizing tasting flavors.

Represents flavor tags in the MyCask application, such as smoky, sweet, spicy,
used to tag and categorize flavors in tastings.
"""

from ..db.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class FlavorTag(Base):
    __tablename__ = "flavor_tags"

    id = Column(Integer, index=True, primary_key=True)
    name = Column(String(50), unique=True, index=True, nullable=False)  # smoky, sweet, spicy

    # Relationships
    tasting_flavors = relationship("TastingFlavor", back_populates="flavor_tag", cascade="all, delete-orphan")

