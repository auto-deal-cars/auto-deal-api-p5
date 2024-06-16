# """Test for the list_available_vehicles function."""
# import json
# from unittest.mock import patch, MagicMock
# import pytest

# from vehicle.adapters.controllers.list_available_vehicles_controller import list_available_vehicles

# mock_vehicles = [
#     MagicMock(model_dump=lambda: {"id": 1, "name": "Vehicle 1"}),
#     MagicMock(model_dump=lambda: {"id": 2, "name": "Vehicle 2"})
# ]

# @pytest.fixture
# def mock_db():
#     """Mock the database."""
#     with patch(
#         'vehicle.adapters.controllers.list_available_vehicles_controller.get_db'
#     ) as mock_get_db:
#         mock_get_db.return_value = iter([MagicMock()])
#         yield mock_get_db

# @pytest.fixture
# def mock_repository():
#     """Mock the repository."""
#     with patch(
#         'vehicle.adapters.controllers.list_available_vehicles_controller.VehicleRepositoryAdapter'
#     ) as mock_repo:
#         yield mock_repo

# @pytest.fixture
# def mock_service():
#     """Mock the service."""
#     with patch(
#         'vehicle.adapters.controllers.list_available_vehicles_controller.VehicleService'
#     ) as mock_service:
#         mock_service_instance = mock_service.return_value
#         mock_service_instance.get_all_available.return_value = mock_vehicles
#         yield mock_service

# def test_list_available_vehicles_success(mock_db, mock_repository, mock_service):
#     """Test the success case."""
#     event = {}
#     context = {}
#     response = list_available_vehicles(event, context)
#     assert response['statusCode'] == 200
#     assert json.loads(
#         response['body']
#     ) == [
#         {"id": 1, "name": "Vehicle 1"},
#         {"id": 2, "name": "Vehicle 2"}
#     ]
