""" Update Vehicle """
import json
from pydantic import ValidationError

from application.services.vehicle_service import VehicleService
from adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from infrastructure.database.setup import get_db

def update_vehicle(event, context):
    """ Update Vehicle """
    try:
        body = json.loads(event.get('body', '{}'))
        vehicle_id = event.get('pathParameters', {}).get('id')
        if not vehicle_id:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'Vehicle ID is required'
                })
            }

        db = next(get_db())
        repository = VehicleRepositoryAdapter(db)
        service = VehicleService(repository)
        service.update_vehicle(vehicle_id, body)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Vehicle updated successfully!',
            })
        }
    except ValidationError as error:
        print(error)
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Validation error'
            })
        }
    except Exception as error:
        print(error)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred while updating the vehicle',
            })
        }
