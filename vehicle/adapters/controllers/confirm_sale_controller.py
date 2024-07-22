""" This module contains the controller for the create vehicle """
import json
import logging

from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.exceptions.vehicle_exceptions import InvalidVehicleIDError
from vehicle.infrastructure.database.setup import get_db
from vehicle.exceptions.exception_handler import event_exception_handlers

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

@event_exception_handlers(logger=logger)
def confirm_sale(event, context):
    """ Confirm a sale for a Vehicle """
    body = json.loads(event["Records"][0]["body"])
    vehicle_id = body["vehicle_id"]

    if not vehicle_id:
        raise InvalidVehicleIDError(
            message="vehicle_id is required",
            status_code=400
        )

    db = next(get_db())
    repository = VehicleRepositoryAdapter(db)
    service = VehicleService(repository)
    service.confirm_sale(vehicle_id)
