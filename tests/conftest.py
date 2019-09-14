import json
import logging
import os.path
from datetime import datetime

import pytest
import rutertider

LOG = logging.getLogger(__name__)


@pytest.fixture
def fixed_datetime():
    class FixedDateTime:
        """A mock of datetime that provides a fixed value for now()"""

        def __init__(self, timestamp):
            if isinstance(timestamp, str):
                self.timestamp = datetime.fromisoformat(timestamp)
            elif isinstance(timestamp, datetime):
                self.timestamp = timestamp

        def now(self, tz=None):
            if tz is None:
                tz = self.timestamp.tzinfo
            return self.timestamp.replace(tzinfo=tz)

        @staticmethod
        def fromisoformat(string):
            return datetime.fromisoformat(string)

    return FixedDateTime


@pytest.fixture
def saved_situation():
    with open(os.path.join(os.path.dirname(__file__), "data",
                           "situation.json")) as file:
        json_data = json.load(file)
    return json_data


@pytest.fixture
def app():
    app = rutertider.create_app()
    return app
