""" Cancel a sale for a Vehicle """

import json
from vehicle.application.services.vehicle_service import VehicleService
from vehicle.adapters.repositories.vehicle_repository_adapter import VehicleRepositoryAdapter
from vehicle.exceptions.exception_handler import http_exception_handler
from vehicle.exceptions.vehicle_exceptions import InvalidVehicleIDError
from vehicle.infrastructure.database.exceptions.orm_exceptions import handle_sqlalchemy_exceptions
from vehicle.infrastructure.database.setup import get_db

@http_exception_handler
@handle_sqlalchemy_exceptions
def cancel_sale(event, context):
    """ Cancel a sale for a Vehicle """
    body = json.loads(event["Records"][0]["body"])
    vehicle_id = body["vehicle_id"]

    if not vehicle_id:
        raise InvalidVehicleIDError(
            message="vehicle_id is required",
            status_code=400
        )

    db = next(get_db())
    repository = VehicleRepositoryAdapter(db)
    service = VehicleService(repository)
    service.revert_sale(vehicle_id)
