"""
This module contains the domain model for the vehicle application.
"""
from pydantic import BaseModel, Field

class Vehicle(BaseModel):
    """
    This class contains the domain model for the vehicle application.
    """
    brand_name: str = Field(..., min_length=1, max_length=100, description="Brand Name")
    model: str = Field(..., min_length=1, max_length=100, description="Model")
    year: int = Field(..., ge=1886, description="Year")
    color: str = Field(..., min_length=1, max_length=50, description="Color")
    price: float = Field(..., gt=0, description="Price")
