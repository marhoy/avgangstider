"""Classes for the avgangstider package."""

from __future__ import annotations

import functools
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Departure:
    """A data class to hold information about a departure."""

    line_id: str
    line_name: str
    destination: str
    platform: str
    departure_datetime: datetime
    bg_color: str
    fg_color: str

    @property
    def departure_string(self) -> str:
        """The departure time as a string relative to now()."""
        # How long is it to the departure?
        now = datetime.now(tz=self.departure_datetime.tzinfo)
        minutes = (self.departure_datetime - now).total_seconds() // 60
        if minutes <= 0:
            departure_string = "nå"
        elif minutes <= 30:
            departure_string = f"{minutes:.0f} min"
        else:
            departure_string = self.departure_datetime.strftime("%H:%M")

        return departure_string

    def __str__(self) -> str:
        """What a departure looks like if you print() it."""
        return (
            f"{self.line_name:2s} -> {self.destination:15s} @ {self.departure_string}"
        )


@dataclass
@functools.total_ordering
class Situation:
    """A data class to hold information about a situation."""

    line_id: str
    line_name: str
    transport_mode: str
    bg_color: str
    fg_color: str
    summary: str

    def __eq__(self, other: object) -> bool:
        """Define what it takes for two Situations to be equal."""
        if not isinstance(other, Situation):
            return NotImplemented
        return (self.line_name, self.summary) == (other.line_name, other.summary)

    def __lt__(self, other: Situation) -> bool:
        """Define what it takes for one Situation to be less than another."""
        return (self.line_name, self.summary) < (other.line_name, other.summary)

    def __str__(self) -> str:
        """What a situation looks like if you print() it."""
        return f"{self.line_name}: {self.summary}"
