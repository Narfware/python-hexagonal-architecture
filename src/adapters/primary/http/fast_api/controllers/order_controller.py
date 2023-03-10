import logging
from fastapi import status, FastAPI
from typing import Optional
from src.adapters.primary.dtos.order_creation import Order_Creation
from src.use_cases.order.create_order.main import Create_Order
from src.adapters.primary.dtos.order import Order
from dependency_injector.wiring import inject, Provide
from containers import Container
from src.adapters.primary.http.fast_api.exception_manager import manage_exception


logger = logging.getLogger(__name__)


@inject
class Order_Controller:
    def __init__(
        self,
        app: FastAPI,
        create_order_use_case: Create_Order = Provide[Container.create_order_use_case],
    ):
        self.app = app
        self.create_order_use_case = create_order_use_case

        @app.post("/orders", status_code=status.HTTP_201_CREATED)
        def create_order(order_data: Order_Creation) -> Optional[str]:
            try:
                order = self.create_order_use_case.execute(
                    "user_id", order_data.product_id
                )
                return order._id
            except Exception as error:
                manage_exception(error)
