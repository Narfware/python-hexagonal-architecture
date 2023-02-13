import datetime
from pydantic import BaseModel


class Order(BaseModel):
    product_id: str
    user_id: str
    status: str
    created_at: datetime.date
