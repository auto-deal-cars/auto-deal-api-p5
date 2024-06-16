"""
This module contains the database models for the AutoDeal application.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, UniqueConstraint
from sqlalchemy.orm import relationship
from vehicle.infrastructure.database.setup import Base

class VehicleBrand(Base):
    """
    Represents a brand of vehicles.
    """
    __tablename__ = 'vehicle_brand'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, unique=True)
    vehicles = relationship('Vehicle', back_populates='brand')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

class Vehicle(Base):
    """
    Represents a vehicle.
    """
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True, index=True)
    brand_id = Column(Integer, ForeignKey('vehicle_brand.id'), nullable=False)
    model = Column(String, index=True, unique=True)
    year = Column(Integer)
    color = Column(String)
    price = Column(Float)
    brand = relationship('VehicleBrand', back_populates='vehicles')
    sold = relationship('VehicleSold', back_populates='vehicle')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    __table_args__ = (UniqueConstraint("model", name="model_key"),)

class VehicleSold(Base):
    """
    Represents a vehicle sold.
    """
    __tablename__ = 'vehicle_sold'
    order_id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'), nullable=False)
    sold_price = Column(Float)
    sold_date = Column(DateTime)
    user_id = Column(Integer)
    vehicle = relationship('Vehicle', back_populates='sold')
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
