"""
This module contains a decorator to handle SQLAlchemy exceptions.
"""
from functools import wraps
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from vehicle.exceptions.vehicle_exceptions import (
    CustomDatabaseException,
    CustomNotFoundException,
    MultipleResultsFoundError,
    VehicleAlreadyExistsError,
)

def handle_sqlalchemy_exceptions(func):
    """
    Decorator to handle SQLAlchemy exceptions.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoResultFound as exception:
            raise CustomNotFoundException(
                message="No result found", status_code=404) from exception
        except MultipleResultsFound as exception:
            raise MultipleResultsFoundError(
                message="Multiple results found", status_code=400) from exception
        except IntegrityError as exception:
            raise VehicleAlreadyExistsError(
                message="Vehicle already exists", status_code=409) from exception
        except SQLAlchemyError as exception:
            raise CustomDatabaseException(
                message="An error occurred", status_code=500) from exception
    return wrapper
