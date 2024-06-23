"""Test for vehicle sold."""
import pytest
from vehicle.domain.entities.vehicle_sold import VehicleSold

@pytest.fixture
def vehicle_sold() -> VehicleSold:
    """Fixture for vehicle sold."""
    return VehicleSold(
        order_id=1,
        vehicle_id=22,
        status="sold",
        sold_price=200000,
        sold_date="2022-01-01",
        user_id="abof",
    )


def test_vehicle_sold(vehicle_sold: VehicleSold) -> None:
    """Test for vehicle sold."""
    assert vehicle_sold.order_id == 1
    assert vehicle_sold.vehicle_id == 22
    assert vehicle_sold.status == "sold"
    assert vehicle_sold.sold_price == 200000
    assert vehicle_sold.sold_date == "2022-01-01"
    assert vehicle_sold.user_id == "abof"

def test_with_invalid_order_id(vehicle_sold: VehicleSold) -> None:
    """Test for vehicle sold with invalid order id."""
    vehicle_sold.order_id = -1
    with pytest.raises(ValueError):
        VehicleSold(
            order_id="a",
            vehicle_id=vehicle_sold.vehicle_id,
            status=vehicle_sold.status,
            sold_price=vehicle_sold.sold_price,
            sold_date=vehicle_sold.sold_date,
            user_id=vehicle_sold.user_id,
        )

def test_with_invalid_vehicle_id(vehicle_sold: VehicleSold) -> None:
    """Test for vehicle sold with invalid vehicle id."""
    with pytest.raises(ValueError):
        VehicleSold(
            order_id=vehicle_sold.order_id,
            vehicle_id="a",
            status=vehicle_sold.status,
            sold_price=vehicle_sold.sold_price,
            sold_date=vehicle_sold.sold_date,
            user_id=vehicle_sold.user_id,
        )
