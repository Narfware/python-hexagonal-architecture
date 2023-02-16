from fastapi import FastAPI
from src.adapters.primary.http.fast_api.controllers.order_controller import (
    Order_Controller,
)
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


class FastApiManager:
    def __init__(self):
        pass

    def initialize(self):
        app = FastAPI()

        FastAPIInstrumentor.instrument_app(app)

        @app.get("/ping")
        def ping():
            return {"Status": "alive"}

        Order_Controller(app)

        return app
