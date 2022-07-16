from dataclasses import dataclass
import datetime
from uuid import UUID


@dataclass
class SalesRecord:
    id: UUID
    category: str
    widget_id: UUID
    customer_name: str
    price: float
    created: datetime.datetime
