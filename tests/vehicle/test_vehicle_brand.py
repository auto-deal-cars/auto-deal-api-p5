"""Test the VehicleBrand entity."""
from datetime import datetime
import pytest

from vehicle.domain.entities.vehicle_brand import VehicleBrand

@pytest.fixture
def vehicle_brand() -> VehicleBrand:
    """Create a VehicleBrand entity."""
    return VehicleBrand(
        id=1,
        name="Test Brand",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )

def test_vehicle_brand(vehicle_brand: VehicleBrand) -> None:
    """Test the VehicleBrand entity."""
    assert vehicle_brand.id == 1
    assert vehicle_brand.name == "Test Brand"

def test_vehicle_invalid_name(vehicle_brand: VehicleBrand) -> None:
    """Test the VehicleBrand entity with invalid name."""
    with pytest.raises(ValueError):
        VehicleBrand(
            name="",
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

def test_vehicle_brand_max_length(vehicle_brand: VehicleBrand) -> None:
    """Test the VehicleBrand entity with max length."""
    with pytest.raises(ValueError):
        VehicleBrand(
            name="test" * 100,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

def test_vehicle_brand_created_at_not_defined(vehicle_brand: VehicleBrand) -> None:
    """Test the VehicleBrand entity with created_at not defined."""
    with pytest.raises(ValueError):
        VehicleBrand(
            name="Test Brand",
            created_at=None,
            updated_at=datetime.now(),
        )

def test_vehicle_brand_updated_at_not_defined(vehicle_brand: VehicleBrand) -> None:
    """Test the VehicleBrand entity with updated_at not defined."""
    with pytest.raises(ValueError):
        VehicleBrand(
            name="Test Brand",
            created_at=datetime.now(),
            updated_at=None,
        )

def test_vehicle_brand_valid_dates(vehicle_brand: VehicleBrand) -> None:
    """Test the VehicleBrand entity with valid dates."""
    assert vehicle_brand.created_at is not None
    assert vehicle_brand.updated_at is not None

def test_vehicle_brand_equality() -> None:
    """Test the equality of VehicleBrand entities."""
    brand1 = VehicleBrand(
        name="Test Brand",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    brand2 = VehicleBrand(
        name="Test Brand",
        created_at=brand1.created_at,
        updated_at=brand1.updated_at,
    )
    assert brand1 == brand2

def test_vehicle_brand_inequality() -> None:
    """Test the inequality of VehicleBrand entities."""
    brand1 = VehicleBrand(
        name="Test Brand",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    brand2 = VehicleBrand(
        name="Another Brand",
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    assert brand1 != brand2

def test_vehicle_brand_update_name(vehicle_brand: VehicleBrand) -> None:
    """Test updating the name of VehicleBrand entity."""
    vehicle_brand.name = "Updated Brand"
    assert vehicle_brand.name == "Updated Brand"
