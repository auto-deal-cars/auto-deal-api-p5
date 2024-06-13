""" This module contains the controller for the create vehicle """
import json
from pydantic import ValidationError

from application.services.vehicle_service import VehicleService
from adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from infrastructure.database.setup import get_db

def register_vehicle(event, context):
    """ Register a new Vehicle """
    try:
        body = json.loads(event.get('body', '{}'))

        db = next(get_db())
        repository = VehicleRepositoryAdapter(db)
        service = VehicleService(repository)
        service.register_vehicle(body)

        return {
            'statusCode': 201,
            'body': json.dumps({
                'message': 'Vehicle created successfully!',
            })
        }
    except ValidationError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Validation error',
                'errors': e.errors()
            })
        }
    except Exception:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred while registering the vehicle',
            })
        }
