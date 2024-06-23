"""
This class contains the repository for the vehicle application.
"""
from typing import List
from datetime import datetime
from sqlalchemy.orm import Session

from vehicle.domain.entities.vehicle import Vehicle as VehicleEntity
from vehicle.domain.entities.vehicle_sold import VehicleSold as VehicleSoldEntity
from vehicle.application.ports.vehicle_repository import VehicleRepository
from vehicle.infrastructure.database.models import Vehicle, VehicleBrand, VehicleSold

class VehicleRepositoryAdapter(VehicleRepository):
    """
    This class contains the repository for the vehicle application.
    """
    def __init__(self, db: Session):
        self.db = db

    def save(self, vehicle: VehicleEntity) -> VehicleEntity:
        """
        Save a vehicle to the database.
        """
        brand = self.get_brand(vehicle.brand_name)
        if brand is None:
            brand = self.create_brand(vehicle.brand_name)

        new_vehicle = Vehicle(
            brand_id=brand.id,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            price=vehicle.price,
        )
        self.db.add(new_vehicle)
        self.db.commit()
        self.db.refresh(new_vehicle)

        return VehicleEntity(
            id=new_vehicle.id,
            brand_name=vehicle.brand_name,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            price=vehicle.price,
        )

    def update(self, vehicle_id: int, vehicle: VehicleEntity) -> VehicleEntity:
        """
        Update a vehicle in the database.
        """
        brand = self.get_brand(vehicle.brand_name)
        if brand is None:
            brand = self.create_brand(vehicle.brand_name)

        self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).update({
            'model': vehicle.model,
            'brand_id': brand.id,
            'year': vehicle.year,
            'color': vehicle.color,
            'price': vehicle.price
        })
        self.db.commit()

        updated_vehicle = self.db.query(
            Vehicle
        ).filter(Vehicle.id == vehicle_id).first()

        return VehicleEntity(
            id=updated_vehicle.id,
            brand_name=updated_vehicle.brand.name,
            model=updated_vehicle.model,
            year=updated_vehicle.year,
            color=updated_vehicle.color,
            price=updated_vehicle.price
        )

    def get(self, vehicle_id: int) -> VehicleEntity:
        """
        Get a vehicle by its id.
        """
        vehicle = self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
        if vehicle is None:
            raise ValueError(f'Vehicle with id {vehicle_id} not found')

        return VehicleEntity(
            id=vehicle.id,
            brand_name=vehicle.brand.name,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            price=vehicle.price
        )

    def get_with_sold(self, vehicle_id: int) -> Vehicle | None:
        """
        Get a vehicle by its id with the sold status.
        """
        vehicle = self.db.query(Vehicle).filter(Vehicle.id == vehicle_id).first()
        return vehicle

    def get_all_available(self) -> List[VehicleEntity]:
        """
        Get all available vehicles from the database.
        """
        vehicles = self.db.query(Vehicle) \
            .filter(Vehicle.sold == None) \
            .order_by(Vehicle.price) \
            .all()

        vehicles_list = [VehicleEntity(
            id=vehicle.id,
            brand_name=vehicle.brand.name,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            price=vehicle.price,
            sold=None
            ) for vehicle in vehicles]

        return vehicles_list

    def get_all_sold(self) -> List[VehicleEntity]:
        """
        Get all sold vehicles from the database.
        """
        vehicles = self.db.query(Vehicle) \
            .filter(Vehicle.sold != None) \
            .order_by(Vehicle.price) \
            .all()

        vehicles_list = [VehicleEntity(
            id=vehicle.id,
            brand_name=vehicle.brand.name,
            model=vehicle.model,
            year=vehicle.year,
            color=vehicle.color,
            price=vehicle.price,
            sold=VehicleSoldEntity(
                order_id=vehicle.sold.order_id,
                vehicle_id=vehicle.sold.vehicle_id,
                status=vehicle.sold.status,
                sold_date=vehicle.sold.sold_date.isoformat(),
                user_id=vehicle.sold.user_id,
                sold_price=vehicle.sold.sold_price,
            ).model_dump() if vehicle.sold else None
            ) for vehicle in vehicles]

        return vehicles_list

    def initialize_sale(self, vehicle: Vehicle, user_id: str) -> None:
        """
        Initialize a sale in the database.
        Marking vehicle as sold and creating a new VehicleSold object.
        """
        sold_vehicle = VehicleSold(
            vehicle_id=vehicle.id,
            sold_price=vehicle.price,
            user_id=user_id,
        )

        self.db.add(sold_vehicle)
        self.db.commit()
        self.db.refresh(sold_vehicle)

        vehicle.sold = sold_vehicle

        self.db.commit()
        self.db.refresh(vehicle)

    def confirm_sale(self, vehicle: Vehicle) -> None:
        """
        Confirm a sale for a vehicle in the database.
        """
        self.db.query(VehicleSold).filter(VehicleSold.vehicle_id == vehicle.id).update({
            'status': 'sold',
            'sold_price': vehicle.price,
            'sold_date': datetime.now(),
        })
        self.db.commit()

    def get_brand(self, brand_name: str) -> VehicleBrand | None:
        """
        Get a brand by its name.
        """
        return self.db.query(
            VehicleBrand
        ).filter(VehicleBrand.name == brand_name).first()

    def create_brand(self, brand_name: str) -> VehicleBrand:
        """
        Create a brand in the database.
        """
        new_brand = VehicleBrand(name=brand_name)

        self.db.add(new_brand)
        self.db.commit()
        self.db.refresh(new_brand)

        return new_brand

    def revert_sale(self, vehicle: Vehicle) -> None:
        """
        Revert a sale for a vehicle in the database.
        """
        vehicle_sold = self.db.query(VehicleSold) \
            .filter(VehicleSold.vehicle_id == vehicle.id) \
            .first()

        if vehicle_sold is None or vehicle_sold.status != "sold":
            raise ValueError(f"Error while reverting sale for vehicle {vehicle.id}")

        self.db.delete(vehicle_sold)
        self.db.commit()
