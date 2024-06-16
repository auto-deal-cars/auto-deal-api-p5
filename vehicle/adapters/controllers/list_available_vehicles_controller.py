""" List Available Vehicles """
import json
from pydantic import ValidationError

from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.infrastructure.database.setup import get_db

def list_available_vehicles(event, context):
    """ List Available Vehicles """
    try:
        db = next(get_db())
        repository = VehicleRepositoryAdapter(db)
        service = VehicleService(repository)
        vehicles = service.get_all_available()

        return {
            'statusCode': 200,
            'body': json.dumps([vehicle.model_dump() for vehicle in vehicles]),
        }
    except ValidationError as error:
        print(error)
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': 'Validation error',
                'errors': error.errors(
                    include_url=False
                )
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
