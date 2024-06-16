""" Get Vehicle """
import json
from pydantic import ValidationError
from sqlalchemy.orm.exc import NoResultFound

from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.infrastructure.database.setup import get_db

def get_vehicle(event, context):
    """ Get Vehicle """
    try:
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
        vehicle = service.get(vehicle_id)

        return {
            'statusCode': 200,
            'body': json.dumps(vehicle.model_dump()),
        }
    except ValidationError as error:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Validation error',
                'errors': error.errors(
                    include_url=False
                )
            })
        }
    except NoResultFound:
        return {
            'statusCode': 404,
            'body': json.dumps({
                'message': 'Vehicle not found'
            })
        }
    except Exception as error:
        print(error)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred while getting the vehicle',
            })
        }
