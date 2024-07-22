"""Handle exceptions in the controller."""
import json
from logging import Logger
from pydantic import ValidationError
from vehicle.exceptions.vehicle_exceptions import (
    CustomDatabaseException,
    CustomNotFoundException,
    InvalidVehicleIDError,
    MultipleResultsFoundError,
    VehicleAlreadyExistsError,
    VehicleNotFoundError,
)

def event_exception_handlers(logger: Logger):
    """Decorator responsible for handling events exceptions in the controller."""
    def decorator(func):
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

def http_exception_handler(func):
    """Decorator responsible for handling HTTP exceptions in the controller."""
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
        except ValueError:
            return {
                'statusCode': 404,
                'body': json.dumps({
                '   message': 'Key error',
                    'error': str(error)
                })
            }
        except Exception:
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'message': 'An error occurred',
                })
            }

    return wrapper
