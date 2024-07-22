""" Get Vehicle """
import json

from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.exceptions.exception_handler import http_exception_handler
from vehicle.exceptions.vehicle_exceptions import InvalidVehicleIDError
from vehicle.infrastructure.database.setup import get_db

@http_exception_handler
def get_vehicle(event, context):
    """ Get Vehicle """
    vehicle_id = event.get('pathParameters', {}).get('id')
    if not vehicle_id:
        raise InvalidVehicleIDError(
            message="vehicle_id is required",
            status_code=400
        )

    db = next(get_db())
    repository = VehicleRepositoryAdapter(db)
    service = VehicleService(repository)
    vehicle = service.get(vehicle_id)

    return {
        'statusCode': 200,
        'body': json.dumps(vehicle.model_dump()),
    }
