"""Handle exceptions in the controller."""
from functools import wraps
import json
from logging import Logger
from typing import Callable
from pydantic import ValidationError
from vehicle.exceptions.vehicle_exceptions import (
    CustomDatabaseException,
    CustomNotFoundException,
    InvalidVehicleIDError,
    MultipleResultsFoundError,
    VehicleAlreadyExistsError,
    VehicleAlreadySoldError,
    VehicleNotFoundError,
    VehicleSaleNotInitializedError,
)

def event_exception_handlers(logger: Logger):
    """Decorator responsible for handling events exceptions in the controller."""
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except ValidationError as error:
                logger.error(f"Validation error: {error.errors(include_url=False)}")
            except InvalidVehicleIDError as error:
                logger.error(f"Invalid vehicle_id: {error}")
            except VehicleNotFoundError as error:
                logger.error(f"Vehicle not found: {error}")
            except CustomNotFoundException as error:
                logger.error(f"Custom not found exception: {error}")
            except MultipleResultsFoundError as error:
                logger.error(f"Multiple results found error: {error}")
            except VehicleAlreadyExistsError as error:
                logger.error(f"Vehicle already exists error: {error}")
            except VehicleSaleNotInitializedError as error:
                logger.error(f"Vehicle sale not initialized error: {error}")
            except VehicleAlreadySoldError as error:
                logger.error(f"Vehicle already sold error: {error}")
            except CustomDatabaseException as error:
                logger.error(f"Custom database exception: {error}")
            except KeyError as error:
                logger.error(f"Key error: {error}")
            except ValueError as error:
                logger.error(f"Value error: {error}")
            except Exception as error:
                logger.error(f"An error occurred: {error}")
        return wrapper
    return decorator

def http_exception_handler(func: Callable):
    """Decorator responsible for handling HTTP exceptions in the controller."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValidationError as error:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    'message': 'Validation error',
                    'errors': error.errors(include_url=False)
                })
            }
        except InvalidVehicleIDError as error:
            return {
                'statusCode': error.status_code,
                'body': json.dumps({
                    'message': error.message,
                    'error': str(error)
                })
            }
        except VehicleAlreadySoldError as error:
            return {
                'statusCode': error.status_code,
                'body': json.dumps({
                    'message': error.message,
                    'error': str(error)
                })
            }
        except VehicleSaleNotInitializedError as error:
            return {
                'statusCode': error.status_code,
                'body': json.dumps({
                    'message': error.message,
                    'error': str(error)
                })
            }
        except VehicleNotFoundError as error:
            return {
                'statusCode': error.status_code,
                'body': json.dumps({
                    'message': error.message,
                    'error': str(error)
                })
            }
        except CustomNotFoundException as error:
            return {
                'statusCode': error.status_code,
                'body': json.dumps({
                    'message': error.message,
                    'error': str(error)
                })
            }
        except MultipleResultsFoundError as error:
            return {
                'statusCode': error.status_code,
                'body': json.dumps({
                    'message': error.message,
                    'error': str(error)
                })
            }
        except CustomDatabaseException as error:
            return {
                'statusCode': error.status_code,
                'body': json.dumps({
                    'message': error.message,
                    'error': str(error)
                })
            }
        except VehicleAlreadyExistsError as error:
            return {
                'statusCode': error.status_code,
                'body': json.dumps({
                    'message': error.message,
                    'error': str(error)
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
        except ValueError as error:
            return {
                'statusCode': 400,
                'body': json.dumps({
                '   message': 'Key error',
                    'error': str(error)
                })
            }
        except Exception as error:
            print(f"An error occurred: {error}")
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'An error occurred',
                })
            }

    return wrapper
