""" This module contains the service for the vehicle application """
from typing import List
from sqlalchemy.orm.exc import NoResultFound

from vehicle.domain.entities.vehicle import Vehicle
from vehicle.application.ports.vehicle_repository import VehicleRepository
from vehicle.infrastructure.database.models import StatusEnum

class VehicleService:
    """ This class contains the service for the vehicle application """
    def __init__(self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def register_vehicle(self, vehicle_data: dict) -> Vehicle:
        """ Register a new Vehicle """
        vehicle = Vehicle(**vehicle_data)

        vehicle = self.vehicle_repository.save(vehicle)

        return vehicle

    def update_vehicle(self, vehicle_id: int, vehicle_data: dict) -> Vehicle:
        """ Update a Vehicle """
        vehicle = self.vehicle_repository.get(vehicle_id)
        if vehicle is None:
            raise NoResultFound(f"Vehicle with ID {vehicle_id} not found")

        vehicle = Vehicle(**vehicle_data)
        vehicle = self.vehicle_repository.update(vehicle_id, vehicle)

        return vehicle

    def get(self, vehicle_id: int) -> Vehicle:
        """ Get a Vehicle by its ID """
        vehicle = self.vehicle_repository.get(vehicle_id)
        if vehicle is None:
            raise NoResultFound(f"Vehicle with ID {vehicle_id} not found")

        return vehicle

    def get_all_available(self) -> List[Vehicle]:
        """ Get all available Vehicles """
        return self.vehicle_repository.get_all_available()

    def get_all_sold(self) -> List[Vehicle]:
        """ Get all sold Vehicles """
        return self.vehicle_repository.get_all_sold()

    def initialize_sale(self, vehicle_id: int, user_id: str) -> None:
        """ Initialize a sale for a Vehicle """
        vehicle = self.vehicle_repository.get_with_sold(vehicle_id)

        if vehicle.sold is not None:
            raise ValueError("Vehicle already sold")

        self.vehicle_repository.initialize_sale(vehicle, user_id)

    def confirm_sale(self, vehicle_id: int) -> None:
        """ Confirm a sale for a Vehicle """
        vehicle = self.vehicle_repository.get_with_sold(vehicle_id)

        print(vehicle.sold.status == StatusEnum.sold)

        if vehicle.sold.status == StatusEnum.sold:
            raise ValueError("Vehicle already sold")

        self.vehicle_repository.confirm_sale(vehicle)

    def revert_sale(self, vehicle_id: int) -> None:
        """ Revert a sale for a Vehicle """
        vehicle = self.vehicle_repository.get_with_sold(vehicle_id)

        if vehicle.sold is None or vehicle.sold.status == StatusEnum.sold:
            raise ValueError("Vehicle sale not initialized or already sold")

        self.vehicle_repository.revert_sale(vehicle)
