""" List Available Vehicles """
import json

from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.exceptions.exception_handler import http_exception_handler
from vehicle.infrastructure.database.exceptions.orm_exceptions import handle_sqlalchemy_exceptions
from vehicle.infrastructure.database.setup import get_db

@http_exception_handler
@handle_sqlalchemy_exceptions
def list_sold_vehicles(event, context):
    """ List Sold Vehicles """
    db = next(get_db())
    repository = VehicleRepositoryAdapter(db)
    service = VehicleService(repository)
    vehicles = service.get_all_sold()

    vehicles_dict = [vehicle.model_dump() for vehicle in vehicles]

    return {
        'statusCode': 200,
        'body': json.dumps(vehicles_dict),
    }
