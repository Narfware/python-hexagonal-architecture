from constants import PRIMARY_ADAPTERS_HTTP
from containers import Container
from src.adapters.primary.http.fast_api.main import FastApiManager
from src.adapters.secondary.tracing.open_telemetry.main import (
    tracer,
)  # Import tracer to start the app instrumentation


# Main method
# Orchestrate the adapters and injections
def main():
    container = Container()  # Initialize main container
    container.wire(
        modules=PRIMARY_ADAPTERS_HTTP
    )  # Inject use cases in the primary adapters

    # Return the Fast APP to be initialized by uvicorn
    return FastApiManager().initialize()
