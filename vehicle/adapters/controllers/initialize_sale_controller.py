""" This module contains the controller for the create vehicle """
import json

from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.exceptions.exception_handler import http_exception_handler
from vehicle.exceptions.vehicle_exceptions import InvalidVehicleIDError
from vehicle.infrastructure.database.exceptions.orm_exceptions import handle_sqlalchemy_exceptions
from vehicle.infrastructure.database.setup import get_db

@http_exception_handler
@handle_sqlalchemy_exceptions
def initialize_sale(event, context):
    """ Initialize a sale for a Vehicle """
    vehicle_id = event.get('pathParameters', {}).get('id')
    user_id = (
        event
        .get('requestContext', {})
        .get('authorizer', {})
        .get('jwt', {})
        .get('claims', {})
        .get('sub')
    )
    access_token = event.get('headers', {}).get('authorization')
    access_token = access_token.replace("Bearer ", "")

    if not vehicle_id or not user_id:
        raise InvalidVehicleIDError(
            message="vehicle_id and user_id are required",
            status_code=400
        )


    db = next(get_db())
    repository = VehicleRepositoryAdapter(db)
    service = VehicleService(repository)
    idempotency_key = service.initialize_sale(
        vehicle_id,
        user_id,
        access_token
    )

    return {
        'statusCode': 201,
        'body': json.dumps({
            'message': 'Initialized sale successfully!',
            'idempotency_key': idempotency_key
        })
    }
