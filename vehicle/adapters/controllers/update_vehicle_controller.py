""" Update Vehicle """
import json

from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.exceptions.exception_handler import http_exception_handler
from vehicle.exceptions.vehicle_exceptions import InvalidVehicleIDError
from vehicle.infrastructure.database.setup import get_db

@http_exception_handler
def update_vehicle(event, context):
    """ Update Vehicle """
    body = json.loads(event.get('body', '{}'))
    vehicle_id = event.get('pathParameters', {}).get('id')

    if not vehicle_id:
        raise InvalidVehicleIDError(
            message="vehicle_id is required",
            status_code=400
        )

    db = next(get_db())
    repository = VehicleRepositoryAdapter(db)
    service = VehicleService(repository)
    vehicle = service.update_vehicle(vehicle_id, body)

    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Vehicle updated successfully!',
            'vehicle': vehicle.model_dump()
        })
    }
