from enum import Enum


class OrderStatus(Enum):
    INITIAL = "Initial",
    PROCESSING = "Processing",
    DELIVER = "Deliver",
    CLOSED = "Closed",
    CANCEL = "Cancel"

