
from fastapi import FastAPI
from src.adapters.primary.http.fast_api.controllers.order_controller import Order_Controller
from src.use_cases.order.create_order.main import Create_Order


class FastApiManager:
    def __init__(self, create_order_use_case: Create_Order):
        self.create_order_use_case = create_order_use_case

    def initialize(self):
        app = FastAPI()
        
        @app.get("/ping")
        def ping():
            return {"Status": "alive"}
        
        Order_Controller(app, self.create_order_use_case)
      
        return app