import logging
from fastapi import status
from fastapi import FastAPI
from src.adapters.primary.dtos.order_creation import Order_Creation
from src.use_cases.order.create_order.main import Create_Order
from src.adapters.secondary.tracing.open_telemetry.decorator import instrument
from src.adapters.secondary.tracing.open_telemetry.main import tracer

logger = logging.getLogger(__name__)


class Order_Controller:
    def __init__(self, app: FastAPI, create_order_use_case: Create_Order):
        self.app = app
        self.create_order_use_case = create_order_use_case

 
        @app.post("/orders", status_code=status.HTTP_201_CREATED)
        def create_order(order: Order_Creation):
            try:
                order = self.create_order_use_case.execute('user_id', order.product_id)
                return order
            except Exception as error:
                   logger.exception(error)
