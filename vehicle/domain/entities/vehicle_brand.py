"""
This module contains the domain model for the vehicle brand.
"""
from datetime import datetime
from pydantic import BaseModel, Field

class VehicleBrand(BaseModel):
    """
    This class contains the domain model for the vehicle brand.
    """
    name: str = Field(..., min_length=1, max_length=100, description="Brand name")
    created_at: datetime = Field(..., description="Creation date")
    updated_at: datetime = Field(..., description="Last update date")
