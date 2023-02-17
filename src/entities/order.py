import datetime
from enum import Enum


class ORDER_STATUS(Enum):
    NEW = "NEW"
    PREPARING = "PREPARING"
    PROCESSING = "PROCESSING"
    DISPATCHING = "DISPATCHING"
    DELIVERING = "DELIVERING"
    SUCCEDED = "SUCCEDED"
    FAILED = "FAILED"


class Order:
    def __init__(
        self,
        _id: str,
        user_id: str,
        product_id: str,
        status: ORDER_STATUS,
        created_at: datetime.date,
    ):
        self._id = _id
        self.user_id = user_id
        self.product_id = product_id
        self.status = status.value
        self.created_at = created_at

    def get_status(self) -> ORDER_STATUS:
        return self.status

    def set_status(self, new_status: ORDER_STATUS) -> None:
        if self.status == ORDER_STATUS.NEW and new_status != ORDER_STATUS.PREPARING:
            raise Exception(
                "Bad status received, cannot change from %s to %d"
                % (self.status, new_status)
            )
        if (
            self.status == ORDER_STATUS.PREPARING
            and new_status != ORDER_STATUS.PROCESSING
        ):
            raise Exception(
                "Bad status received, cannot change from %s to %d"
                % (self.status, new_status)
            )
        if (
            self.status == ORDER_STATUS.PROCESSING
            and new_status != ORDER_STATUS.DISPATCHING
        ):
            raise Exception(
                "Bad status received, cannot change from %s to %d"
                % (self.status, new_status)
            )
        if (
            self.status == ORDER_STATUS.DISPATCHING
            and new_status != ORDER_STATUS.DELIVERING
        ):
            raise Exception(
                "Bad status received, cannot change from %s to %d"
                % (self.status, new_status)
            )
        self.status = new_status
