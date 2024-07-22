"""
This module contains the domain model for the vehicle application.
"""
from typing import Optional, Union
from pydantic import BaseModel, Field

from vehicle.domain.entities.vehicle_sold import VehicleSold

class Vehicle(BaseModel):
    """
    This class contains the domain model for the vehicle application.
    """
    id: Optional[int] = Field(default=None, description="Vehicle ID")
    brand_name: str = Field(..., min_length=1, max_length=100, description="Brand Name")
    model: str = Field(..., min_length=1, max_length=100, description="Model")
    quantity: int = Field(..., gt=0, description="Quantity")
    year: int = Field(..., ge=1886, description="Year")
    color: str = Field(..., min_length=1, max_length=50, description="Color")
    price: float = Field(..., gt=0, description="Price")
    sold: Optional[Union[dict, VehicleSold]] = Field(default=None, description="Vehicle sold")
