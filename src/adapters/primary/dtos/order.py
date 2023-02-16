import datetime
from pydantic import BaseModel

from src.entities.order import ORDER_STATUS


class Order(BaseModel):
    product_id: str
    user_id: str
    status: ORDER_STATUS
    created_at: datetime.date
