from pydantic import BaseModel


class Order_Creation(BaseModel):
    product_id: str
