from enum import Enum


class RetrieveAggregateUsagePeriod(str, Enum):
    DAY = "day"
    HOUR = "hour"

    def __str__(self) -> str:
        return str(self.value)
