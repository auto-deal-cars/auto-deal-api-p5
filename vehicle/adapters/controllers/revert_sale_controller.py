""" This module contains the controller for the create vehicle """
import json
from pydantic import ValidationError

from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.infrastructure.database.setup import get_db

def revert_sale(event, context):
    """ Revert a sale for a Vehicle """
    try:
        vehicle_id = event.get('pathParameters', {}).get('id')
        if not vehicle_id:
            raise KeyError('Vehicle ID is required')

        db = next(get_db())
        repository = VehicleRepositoryAdapter(db)
        service = VehicleService(repository)
        service.revert_sale(vehicle_id)

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Reverted sale successfully!',
            })
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
    except KeyError as error:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Key error',
                'error': str(error)
            })
        }
    except ValueError:
        return {
            'statusCode': 404,
            'body': json.dumps({
                'message': 'Vehicle not found'
            })
        }
    except Exception as e:
        print(e)
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': 'An error occurred while reverting the sale',
            })
        }
