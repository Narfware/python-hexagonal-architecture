from src.ports.id_generator import IId_generator
from src.repositories.order_repository import Order_Repository
from src.entities.order import Order, ORDER_STATUS
from datetime import datetime
from src.adapters.secondary.tracing.open_telemetry.decorator import instrument

@instrument
class Create_Order:
    def __init__(self, order_repository: Order_Repository, id_generator: IId_generator):
        self.order_repository = order_repository
        self.id_generator = id_generator

    def execute(self, user_id: str, product_id: str) -> Order:
        
        orders = self.order_repository.get_by_user_id(user_id)

        order_in_process = any(order.get_status() != ORDER_STATUS.NEW for order in orders)

        if (order_in_process): raise Exception('Only one simultaneous order is allowed')

        new_order = Order(_id=self.id_generator.generate(), user_id=user_id, product_id=product_id, status="NEW", created_at=datetime.now() )

        self.order_repository.save(new_order)

        return new_order