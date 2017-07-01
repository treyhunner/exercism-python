from datetime import date, datetime, time, timedelta


class Clock:
    def __init__(self, hours: int, minutes: int) -> None:
        start: datetime = datetime.combine(date.today(), time(0, 0))
        self.dt: datetime = start + timedelta(hours=hours, minutes=minutes)

    def add(self, minutes: int) -> str:
        self.dt += timedelta(minutes=minutes)
        return self.dt.strftime('%H:%M')

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Clock):
            return NotImplemented
        return (self.dt.time() == other.dt.time())

    def __str__(self) -> str:
        return self.dt.strftime('%H:%M')
