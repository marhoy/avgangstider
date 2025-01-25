"""Defines fixtures for the test suite."""

from __future__ import annotations

import json
import logging
import pickle
from pathlib import Path
from typing import Any

import pytest
from flask import Flask
from pydantic import Json

import avgangstider
from avgangstider.classes import Situation

LOG = logging.getLogger(__name__)


@pytest.fixture
def saved_situations_json() -> Json[Any]:  # noqa: D103
    with Path(Path(__file__).parent / "data" / "situations.json").open() as file:
        return json.load(file)


@pytest.fixture
def saved_situations_list() -> list[Situation]:  # noqa: D103
    with Path(Path(__file__).parent / "data" / "situations.pkl").open("rb") as file:
        return pickle.load(file)  # noqa: S301


@pytest.fixture
def app() -> Flask:  # noqa: D103
    return avgangstider.create_app()
