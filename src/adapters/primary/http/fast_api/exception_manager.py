import logging
from fastapi import HTTPException, status
from src.exceptions.simultaneous_order import Simultaneous_order_error

logger = logging.getLogger(__name__)

def manage_exception(exception: Exception) -> None:
    if isinstance(exception, Simultaneous_order_error):
        logger.warning(exception)
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exception))
    else: 
        logger.exception(exception)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    