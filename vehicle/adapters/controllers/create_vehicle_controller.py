""" This module contains the controller for the create vehicle """
import json

from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.exceptions.exception_handler import http_exception_handler
from vehicle.infrastructure.database.setup import get_db

@http_exception_handler
def register_vehicle(event, context):
    """ Register a new Vehicle """
    body = json.loads(event.get('body', '{}'))

    db = next(get_db())
    repository = VehicleRepositoryAdapter(db)
    service = VehicleService(repository)
    vehicle = service.register_vehicle(body)

    return {
        'statusCode': 201,
        'body': json.dumps({
            'message': 'Vehicle created successfully!',
            'vehicle': vehicle.model_dump()
        })
    }
