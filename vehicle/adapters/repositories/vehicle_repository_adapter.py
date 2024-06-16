"""
This class contains the repository for the vehicle application.
"""
from typing import List
from sqlalchemy.orm import Session

from vehicle.domain.entities.vehicle import Vehicle as VehicleEntity
from vehicle.application.ports.vehicle_repository import VehicleRepository
from vehicle.infrastructure.database.models import Vehicle, VehicleBrand

class VehicleRepositoryAdapter(VehicleRepository):
    """
    This class contains the repository for the vehicle application.
    """
    def __init__(self, db: Session):
        self.db = db

    def save(self, vehicle: VehicleEntity) -> None:
        """
        Save a vehicle to the database.
        """
        brand = self.db.query(VehicleBrand).filter(VehicleBrand.name == vehicle.brand_name).first()
        if brand is None:
            db_vehicle_brand = VehicleBrand(name=vehicle.brand_name)
            self.db.add(db_vehicle_brand)
            self.db.commit()
            self.db.refresh(db_vehicle_brand)
            vehicle.brand_id = db_vehicle_brand.id

        db_vehicle = Vehicle(
            brand_id=brand.id if brand else db_vehicle_brand.id,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            price=vehicle.price
        )
        self.db.add(db_vehicle)
        self.db.commit()
        self.db.refresh(db_vehicle)

    def update(self, vehicle_id: int, vehicle: VehicleEntity) -> None:
        """
        Update a vehicle in the database.
        """
        brand = self.db.query(VehicleBrand).filter(VehicleBrand.name == vehicle.brand_name).first()
        if brand is None:
            db_vehicle_brand = VehicleBrand(name=vehicle.brand_name)
            self.db.add(db_vehicle_brand)
            self.db.commit()
            self.db.refresh(db_vehicle_brand)
            vehicle.brand_id = db_vehicle_brand.id

        self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).update({
            'model': vehicle.model,
            'brand_id': brand.id if brand else vehicle.brand_id,
            'year': vehicle.year,
            'color': vehicle.color,
            'price': vehicle.price
        })
        updated_vehicle = self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
        self.db.refresh(updated_vehicle)

    def get(self, vehicle_id: int) -> VehicleEntity:
        """
        Get a vehicle by its id.
        """
        vehicle = self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
        if vehicle is None:
            raise ValueError(f'Vehicle with id {vehicle_id} not found')

        return VehicleEntity(
            brand_name=vehicle.brand.name,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            price=vehicle.price
        )

    def get_all_available(self) -> List[VehicleEntity]:
        """
        Get all available vehicles from the database.
        """
        vehicles = self.db.query(Vehicle).filter(Vehicle.sold is False).all()

        return [VehicleEntity(
            brand_name=vehicle.brand.name,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            price=vehicle.price
        ) for vehicle in vehicles]
