""" This module contains the service for the vehicle application """
from typing import List
import json
import uuid
import os
import boto3

from sqlalchemy.orm.exc import NoResultFound

from vehicle.domain.entities.vehicle import Vehicle
from vehicle.application.ports.vehicle_repository import VehicleRepository
from vehicle.infrastructure.database.models import StatusEnum

sqs = boto3.client("sqs", region_name="us-east-1")
initialize_payment_queue_url = os.getenv("INITIALIZE_PAYMENT_QUEUE_URL")

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

    def initialize_sale(self, vehicle_id: int, user_id: str) -> str:
        """ Initialize a sale for a Vehicle """
        vehicle = self.vehicle_repository.get_with_sold(vehicle_id)

        if vehicle.sold is not None:
            raise ValueError("Vehicle already sold")

        updated_vehicle = self.vehicle_repository.initialize_sale(vehicle, user_id)
        idempotency_key = str(uuid.uuid4())

        sqs.send_message(
            QueueUrl=initialize_payment_queue_url,
            MessageBody=json.dumps({
                "vehicle_id": updated_vehicle.id,
                "order_id": updated_vehicle.sold.order_id,
                "idempotency_key": idempotency_key,
            }),
        )

        return idempotency_key

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

        if vehicle.sold is None:
            raise ValueError("Vehicle sale not initialized")

        if vehicle.sold.status == StatusEnum.sold:
            raise ValueError("Vehicle already sold")

        self.vehicle_repository.revert_sale(vehicle)
