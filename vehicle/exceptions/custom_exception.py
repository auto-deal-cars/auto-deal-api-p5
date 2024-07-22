"""Custom exception class for handling errors in the vehicle module."""

class CustomException(Exception):
    """Custom exception class for handling errors in the vehicle module."""
    def __init__(self, message: str, status_code: int = 500) -> None:
        super().__init__(message)
        self.status_code = status_code
        self.message = message
