"""
TastingFlavor model for associating flavors with tastings.

Represents the many-to-many relationship between tastings and flavor tags
in the MyCask application, including intensity ratings for each flavor.
"""

from ..db.database import Base
from sqlalchemy import Column, Integer, ForeignKey, CheckConstraint
from sqlalchemy.orm import relationship
from .tasting import Tasting
from .flavor_tags import FlavorTag

class TastingFlavor(Base):
    __tablename__ = "tasting_flavors"
    __table_args__ = (
        CheckConstraint('intensity >= 1 AND intensity <= 5', name='check_intensity_range'),
    )

    tasting_id = Column(Integer, ForeignKey(Tasting.id, ondelete="CASCADE"), primary_key=True)
    flavor_tag_id = Column(Integer, ForeignKey(FlavorTag.id, ondelete="CASCADE"), primary_key=True)
    intensity = Column(Integer, nullable=False)  # CHECK 1-5

    # Relationships
    tasting = relationship("Tasting", back_populates="tasting_flavors")
    flavor_tag = relationship("FlavorTag", back_populates="tasting_flavors")

