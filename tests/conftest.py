"""Defines fixtures for the test suite."""

from __future__ import annotations

import datetime
import json
import logging
import pickle
from pathlib import Path

import pytest
from flask import Flask

import avgangstider
from avgangstider.classes import Situation

LOG = logging.getLogger(__name__)


class FixedDateTime:
    """A mock of datetime that provides a fixed value for now()."""

    def __init__(self, timestamp: str | datetime.datetime) -> None:  # noqa: D107
        if isinstance(timestamp, str):
            self.timestamp = datetime.datetime.fromisoformat(timestamp)
        elif isinstance(timestamp, datetime.datetime):
            self.timestamp = timestamp

    def now(self, tz: datetime.tzinfo | None = None) -> datetime.datetime:  # noqa: D102
        if tz is None:
            tz = self.timestamp.tzinfo
        return self.timestamp.replace(tzinfo=tz)

    @staticmethod
    def fromisoformat(string: str) -> datetime.datetime:  # noqa: D102
        return datetime.datetime.fromisoformat(string)


@pytest.fixture
def fixed_datetime() -> type[FixedDateTime]:  # noqa: D103
    return FixedDateTime


@pytest.fixture
def saved_situations_json() -> dict[str, list[dict[str, str]]]:  # noqa: D103
    with Path(Path(__file__).parent / "data" / "situations.json").open() as file:
        return json.load(file)


@pytest.fixture
def saved_situations_list() -> list[Situation]:  # noqa: D103
    with Path(Path(__file__).parent / "data" / "situations.pkl").open("rb") as file:
        return pickle.load(file)  # noqa: S301


@pytest.fixture
def app() -> Flask:  # noqa: D103
    return avgangstider.create_app()
