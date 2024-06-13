"""
This module contains the repository for the vehicle application.
"""
from abc import ABC, abstractmethod

from typing import List
from domain.entities.vehicle import Vehicle

class VehicleRepository(ABC):
    """
    This class contains the repository for the vehicle application.
    """
    @abstractmethod
    def save(self, vehicle: Vehicle) -> None:
        """
        This method saves a vehicle to the database.
        """
        pass

    @abstractmethod
    def update(self, vehicle: Vehicle) -> None:
        """
        This method updates a vehicle in the database.
        """
        pass

    @abstractmethod
    def get(self, vehicle_id: int) -> Vehicle:
        """
        This method gets a vehicle from the database.
        """
        pass

    def get_all(self) -> List[Vehicle]:
        """
        This method gets all vehicles from the database.
        """
        pass
