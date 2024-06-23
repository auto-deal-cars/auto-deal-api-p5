"""Vehicle sold entity"""
from typing import Optional
from pydantic import BaseModel, Field

class VehicleSold(BaseModel):
    """Vehicle sold entity"""
    order_id: Optional[int] = Field(default=None, description="Order id")
    vehicle_id: int = Field(..., description="Vehicle id")
    status: str = Field(..., description="Status")
    sold_price: float = Field(..., description="Sold price")
    sold_date: Optional[str] = Field(default=None, description="Sold date")
    user_id: str = Field(..., description="User id")
    created_at: Optional[str] = Field(default=None, description="Created at")
    updated_at: Optional[str] = Field(default=None, description="Updated at")
