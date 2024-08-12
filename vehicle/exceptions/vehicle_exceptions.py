"""
    Vehicle Exceptions
"""

from vehicle.exceptions.custom_exception import CustomException


class VehicleNotFoundError(CustomException):
    """
    Vehicle Not Found Error
    """
    pass

class InvalidVehicleIDError(CustomException):
    """
    Invalid Vehicle ID Error
    """
    pass

class CustomNotFoundException(CustomException):
    """
    Custom Not Found Exception
    """
    pass

class MultipleResultsFoundError(CustomException):
    """
    Multiple Results Found Error
    """
    pass

class CustomDatabaseException(CustomException):
    """
    Custom Database Exception
    """
    pass

class VehicleAlreadyExistsError(CustomException):
    """
    Vehicle Already Exists Error
    """
    pass

class VehicleAlreadySoldError(CustomException):
    """
    Vehicle Already Sold Error
    """
    pass

class VehicleSaleNotInitializedError(CustomException):
    """
    Vehicle Sale Not Initialized Error
    """
    pass
