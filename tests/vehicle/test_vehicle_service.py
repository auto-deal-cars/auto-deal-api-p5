"""Test for VehicleService."""
from unittest.mock import create_autospec, patch
import pytest

from vehicle.domain.entities.vehicle import Vehicle
from vehicle.application.services.vehicle_service import VehicleService
from vehicle.application.ports.vehicle_repository import VehicleRepository
from vehicle.domain.entities.vehicle_sold import VehicleSold

@pytest.fixture
def vehicle_repository() -> VehicleRepository:
    """Fixture for VehicleRepository."""
    vehicle_repository = create_autospec(VehicleRepository)

    return vehicle_repository

@pytest.fixture
def vehicle_service(vehicle_repository) -> VehicleService:
    """Fixture for VehicleService."""
    vehicle_service = VehicleService(vehicle_repository)

    return vehicle_service

@pytest.fixture
def mocked_vehicle() -> dict:
    """Fixture for mocked vehicle."""
    return {
        "brand_name": "Toyota",
        "model": "Prius",
        "year": 2022,
        "color": "red",
        "price": 200000,
        "sold": None,
    }

@pytest.fixture
def mocked_vehicle_entity(mocked_vehicle: dict) -> Vehicle:
    """Fixture for mocked vehicle entity."""
    return Vehicle(
        brand_name=mocked_vehicle.get("brand_name"),
        model=mocked_vehicle.get("model"),
        year=mocked_vehicle.get("year"),
        color=mocked_vehicle.get("color"),
        price=mocked_vehicle.get("price"),
        sold=None
    )

@pytest.fixture
def mocked_vehicle_entity_with_sold(mocked_vehicle: dict) -> Vehicle:
    """Fixture for mocked vehicle entity with sold."""
    return Vehicle(
        id=1,
        brand_name=mocked_vehicle.get("brand_name"),
        model=mocked_vehicle.get("model"),
        year=mocked_vehicle.get("year"),
        color=mocked_vehicle.get("color"),
        price=mocked_vehicle.get("price"),
        sold=VehicleSold(
            order_id=2,
            vehicle_id=1,
            status="draft",
            sold_price=200000,
            user_id="22"
        )
    )

def test_get_vehicle(
        vehicle_repository: VehicleRepository,
        vehicle_service: VehicleService,
        mocked_vehicle_entity: Vehicle,
        mocked_vehicle: dict,
    ) -> None:
    """Test for get_vehicle."""
    vehicle_service.get(1)

    vehicle_repository.get.assert_called_once_with(1)

def test_create_vehicle(
        vehicle_repository: VehicleRepository,
        vehicle_service: VehicleService,
        mocked_vehicle_entity: Vehicle,
        mocked_vehicle: dict,
    ) -> None:
    """Test for create_vehicle."""
    vehicle_service.register_vehicle(
        mocked_vehicle,
    )

    vehicle_repository.save.assert_called_once_with(
        mocked_vehicle_entity,
    )

def test_update_vehicle(
        vehicle_repository: VehicleRepository,
        vehicle_service: VehicleService,
        mocked_vehicle_entity: Vehicle,
        mocked_vehicle: dict,
    ) -> None:
    """Test for update_vehicle."""
    mocked_vehicle_entity_id = 1
    vehicle_service.update_vehicle(
        mocked_vehicle_entity_id,
        mocked_vehicle,
    )

    vehicle_repository.update.assert_called_once_with(
        mocked_vehicle_entity_id,
        mocked_vehicle_entity,
    )

def test_get_all_available(
        vehicle_repository: VehicleRepository,
        vehicle_service: VehicleService,
        mocked_vehicle_entity: Vehicle,
        mocked_vehicle: dict,
    ) -> None:
    """Test for get_all_available."""
    vehicle_service.get_all_available()

    vehicle_repository.get_all_available.assert_called_once()

def test_get_all_sold(
        vehicle_repository: VehicleRepository,
        vehicle_service: VehicleService,
        mocked_vehicle_entity: Vehicle,
        mocked_vehicle: dict,
    ) -> None:
    """Test for get_all_sold."""
    vehicle_service.get_all_sold()

    vehicle_repository.get_all_sold.assert_called_once()

def test_initialize_sale(
        vehicle_repository: VehicleRepository,
        vehicle_service: VehicleService,
        mocked_vehicle_entity: Vehicle,
        mocked_vehicle_entity_with_sold: Vehicle
    ) -> None:
    """Test for initialize_sale."""
    with patch.object(
        vehicle_repository,
            "get_with_sold",
            return_value=mocked_vehicle_entity,
        ), patch(
            "vehicle.application.services.vehicle_service.sqs.send_message"
        ), patch(
            "uuid.uuid4", return_value="mocked-uuid"
        ), patch.object(
            vehicle_repository,
            'initialize_sale',
            return_value=mocked_vehicle_entity_with_sold
        ):
        vehicle_service.initialize_sale(22, 1)
        vehicle_repository.initialize_sale.assert_called_once()
