from constants import PRIMARY_ADAPTERS_HTTP, PRIMARY_ADAPTERS_QUEUE
from src.adapters.secondary.databases.mongo.main import Mongo_Client
from containers import Container
from src.adapters.primary.http.fast_api.main import FastApiManager


# Main method
# Orchestrate the adapters and injections
def main():
    container = Container()  # Initialize main container
    container.wire(
        modules=PRIMARY_ADAPTERS_HTTP
    )  # Inject use cases in the primary adapters

    # Return the Fast APP to be initialized by uvicorn
    return (
        FastApiManager().initialize()
    )
