"""Test the Vehicle entity."""
import pytest
from vehicle.domain.entities.vehicle import Vehicle

@pytest.fixture
def vehicle() -> Vehicle:
    """Create a Vehicle entity."""
    return Vehicle(
        id=1,
        brand_name="Test Brand",
        model="Test Model",
        year=2021,
        color="Test Color",
        price=10000,
    )

def test_vehicle(vehicle: Vehicle) -> None:
    """Test the Vehicle entity."""
    assert vehicle.id == 1
    assert vehicle.brand_name == "Test Brand"
    assert vehicle.model == "Test Model"
    assert vehicle.year == 2021
    assert vehicle.color == "Test Color"
    assert vehicle.price == 10000

def test_vehicle_with_invalid_brand_name(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with invalid brand name."""
    with pytest.raises(ValueError):
        Vehicle(
            brand_name="",
            model="Test Model",
            year=2021,
            color="Test Color",
            price=10000,
        )

def test_vehicle_reached_max_brand_name_length(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with reached max brand name length."""
    with pytest.raises(ValueError):
        Vehicle(
            brand_name="test" * 100,
            model="Test Model",
            year=2021,
            color="Test Color",
            price=10000,
        )

    with pytest.raises(ValueError):
        Vehicle(
            brand_name="Test Brand",
            model="",
            year=2021,
            color="Test Color",
            price=10000,
        )

def test_vehicle_invalid_model(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with invalid model."""
    with pytest.raises(ValueError):
        Vehicle(
            brand_name="Test Brand",
            model="",
            year=2021,
            color="Test Color",
            price=10000,
        )

def test_vehicle_invalid_model_length(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with invalid model length."""
    with pytest.raises(ValueError):
        Vehicle(
            brand_name="Test Brand",
            model="test" * 100,
            year=2021,
            color="Test Color",
            price=10000,
        )

def test_vehicle_with_invalid_year(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with invalid year."""
    with pytest.raises(ValueError):
        Vehicle(
            brand_name="Test Brand",
            model="Test Model",
            year=0,
            color="Test Color",
            price=10000,
        )

def test_vehicle_with_invalid_color(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with invalid color."""
    with pytest.raises(ValueError):
        Vehicle(
            brand_name="Test Brand",
            model="Test Model",
            year=2021,
            color="",
            price=10000,
        )

def test_vehicle_with_invalid_color_length(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with invalid color length."""
    with pytest.raises(ValueError):
        Vehicle(
            brand_name="Test Brand",
            model="Test Model",
            year=2021,
            color="test" * 100,
            price=10000,
        )

def test_vehicle_with_invalid_price(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with invalid price."""
    with pytest.raises(ValueError):
        Vehicle(
            brand_name="Test Brand",
            model="Test Model",
            year=2021,
            color="Test Color",
            price=0,
        )

def test_vehicle_with_min_valid_year(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with the minimum valid year."""
    vehicle = Vehicle(
        brand_name="Test Brand",
        model="Test Model",
        year=1886,
        color="Test Color",
        price=10000,
    )
    assert vehicle.year == 1886

def test_vehicle_with_max_valid_year(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with the maximum valid year."""
    vehicle = Vehicle(
        brand_name="Test Brand",
        model="Test Model",
        year=9999,
        color="Test Color",
        price=10000,
    )
    assert vehicle.year == 9999

def test_vehicle_with_min_valid_price(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with the minimum valid price."""
    vehicle = Vehicle(
        brand_name="Test Brand",
        model="Test Model",
        year=2021,
        color="Test Color",
        price=1,
    )
    assert vehicle.price == 1

def test_vehicle_with_max_valid_price(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with the maximum valid price."""
    vehicle = Vehicle(
        brand_name="Test Brand",
        model="Test Model",
        year=2021,
        color="Test Color",
        price=1000000,
    )
    assert vehicle.price == 1000000

def test_vehicle_with_min_valid_brand_name_length(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with the minimum valid brand name length."""
    vehicle = Vehicle(
        brand_name="A",
        model="Test Model",
        year=2021,
        color="Test Color",
        price=10000,
    )
    assert vehicle.brand_name == "A"

def test_vehicle_with_max_valid_brand_name_length(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with the maximum valid brand name length."""
    max_length_brand_name = "A" * 100
    vehicle = Vehicle(
        brand_name=max_length_brand_name,
        model="Test Model",
        year=2021,
        color="Test Color",
        price=10000,
    )
    assert vehicle.brand_name == max_length_brand_name

def test_vehicle_with_min_valid_model_length(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with the minimum valid model length."""
    vehicle = Vehicle(
        brand_name="Test Brand",
        model="A",
        year=2021,
        color="Test Color",
        price=10000,
    )
    assert vehicle.model == "A"

def test_vehicle_with_max_valid_model_length(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with the maximum valid model length."""
    max_length_model = "A" * 100
    vehicle = Vehicle(
        brand_name="Test Brand",
        model=max_length_model,
        year=2021,
        color="Test Color",
        price=10000,
    )
    assert vehicle.model == max_length_model

def test_vehicle_with_min_valid_color_length(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with the minimum valid color length."""
    vehicle = Vehicle(
        brand_name="Test Brand",
        model="Test Model",
        year=2021,
        color="A",
        price=10000,
    )
    assert vehicle.color == "A"

def test_vehicle_with_max_valid_color_length(vehicle: Vehicle) -> None:
    """Test the Vehicle entity with the maximum valid color length."""
    max_length_color = "A" * 50
    vehicle = Vehicle(
        brand_name="Test Brand",
        model="Test Model",
        year=2021,
        color=max_length_color,
        price=10000,
    )
    assert vehicle.color == max_length_color
