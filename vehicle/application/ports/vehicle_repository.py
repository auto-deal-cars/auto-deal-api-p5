"""
This module contains the repository for the vehicle application.
"""
from abc import ABC, abstractmethod

from typing import List
from vehicle.domain.entities.vehicle import Vehicle as VehicleEntity
from vehicle.domain.entities.vehicle_brand import VehicleBrand
from vehicle.infrastructure.database.models import Vehicle

class VehicleRepository(ABC):
    """
    This class contains the repository for the vehicle application.
    """
    @abstractmethod
    def save(self, vehicle: VehicleEntity) -> VehicleEntity:
        """
        This method saves a vehicle to the database.
        """
        pass

    @abstractmethod
    def update(self, vehicle_id: int, vehicle: VehicleEntity) -> VehicleEntity:
        """
        This method updates a vehicle in the database.
        """
        pass

    @abstractmethod
    def get(self, vehicle_id: int) -> VehicleEntity:
        """
        This method gets a vehicle from the database.
        """
        pass

    @abstractmethod
    def get_with_sold(self, vehicle_id: int) -> Vehicle:
        """
        This method gets a vehicle from the database with the sold status.
        """
        pass

    @abstractmethod
    def get_all_available(self) -> List[VehicleEntity]:
        """
        This method gets all available vehicles from the database.
        """
        pass

    @abstractmethod
    def get_all_sold(self) -> List[VehicleEntity]:
        """
        This method gets all sold vehicles from the database.
        """
        pass

    @abstractmethod
    def initialize_sale(self, vehicle: Vehicle, user_id: str) -> None:
        """
        This method initializes a sale for a vehicle in the database.
        """
        pass

    @abstractmethod
    def confirm_sale(self, vehicle: Vehicle) -> None:
        """
        This method confirms a sale for a vehicle in the database.
        """
        pass

    @abstractmethod
    def revert_sale(self, vehicle: Vehicle) -> None:
        """
        This method reverts a sale for a vehicle in the database.
        """
        pass

    @abstractmethod
    def get_brand(self, brand_name: str) -> VehicleBrand | None:
        """
        This method gets a brand from the database.
        """
        pass

    @abstractmethod
    def create_brand(self, brand_name: str) -> VehicleBrand:
        """
        This method creates a brand in the database.
        """
        pass
