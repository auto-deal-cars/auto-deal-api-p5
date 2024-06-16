""" This module contains the service for the vehicle application """
from typing import List

from vehicle.domain.entities.vehicle import Vehicle
from vehicle.application.ports.vehicle_repository import VehicleRepository

class VehicleService:
    """ This class contains the service for the vehicle application """
    def __init__(self, vehicle_repository: VehicleRepository):
        self.vehicle_repository = vehicle_repository

    def register_vehicle(self, vehicle_data: dict) -> None:
        """ Register a new Vehicle """
        vehicle = Vehicle(**vehicle_data)

        self.vehicle_repository.save(vehicle)

    def update_vehicle(self, vehicle_id: int, vehicle_data: dict) -> None:
        """ Update a Vehicle """
        vehicle = Vehicle(**vehicle_data)

        self.vehicle_repository.update(vehicle_id, vehicle)

    def get(self, vehicle_id: int) -> Vehicle:
        """ Get a Vehicle by its ID """
        vehicle = self.vehicle_repository.get(vehicle_id)
        return vehicle

    def get_all_available(self) -> List[Vehicle]:
        """ Get all available Vehicles """
        return self.vehicle_repository.get_all_available()
