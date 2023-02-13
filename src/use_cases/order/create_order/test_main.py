import datetime
from entities.order import Order
from use_cases.order.create_order.main import Create_Order
from tests.mocks.ports.id_generator_mock import Id_generator_mock
from tests.mocks.repositories.order_repository_mock import Order_Repository_Mock
from unittest.mock import ANY, patch
import pytest


def test_should_create_an_order_succesfully():
    with (
        patch.object(Order_Repository_Mock, "get_by_user_id", return_value=[]),
        patch.object(Order_Repository_Mock, "save", return_value=None),
        patch.object(Id_generator_mock, "generate", return_value="123"),
    ):
        use_case = Create_Order(Order_Repository_Mock(), Id_generator_mock())

        result = use_case.execute("user_id", "product_id")

        assert result.__dict__ == {
            "_id": "123",
            "user_id": "user_id",
            "product_id": "product_id",
            "status": "NEW",
            "created_at": ANY,
        }


def test_should_return_an_error_if_an_already_order_is_in_process():
    order_data = Order(
        _id="321",
        user_id="user_id",
        product_id="product_id",
        status="PREPARING",
        created_at=datetime.datetime.now(),
    )

    with (
        patch.object(
            Order_Repository_Mock, "get_by_user_id", return_value=[order_data]
        ),
        patch.object(Order_Repository_Mock, "save", return_value=None),
        patch.object(Id_generator_mock, "generate", return_value="123"),
    ):
        use_case = Create_Order(Order_Repository_Mock(), Id_generator_mock())

        with pytest.raises(Exception):
            use_case.execute("user_id", "product_id")
