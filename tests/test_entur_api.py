"""Tests for the entur_api module."""

from collections.abc import Callable
from unittest import mock

import avgangstider
from avgangstider import entur_api
from avgangstider.classes import Situation

from .conftest import FixedDateTime


def test_get_departures() -> None:  # noqa: D103
    # Test with an empty string as stop_id_
    departures = avgangstider.get_departures(stop_id="")
    assert departures == []

    # Test without specifying line_ids
    # At Godlia T, the only passing line is 3, and there is only two quays
    departures = avgangstider.get_departures(
        stop_id="NSR:StopPlace:5968", max_departures=10
    )
    assert len(departures) == 10
    for departure in departures:
        assert departure.line_name == "3"
        assert departure.platform in ("NSR:Quay:10948", "NSR:Quay:10949")

    # Test querying a specific line (from Helsfyr)
    departures = avgangstider.get_departures(
        "NSR:StopPlace:59516", max_departures=10, line_ids=["RUT:Line:21"]
    )
    assert len(departures) == 10
    for departure in departures:
        assert departure.line_name == "21"

    # Test querying a specific platform (Godlia T, only towards Mortensrud)
    departures = avgangstider.get_departures(
        stop_id="NSR:StopPlace:5968", platforms=["NSR:Quay:10948"]
    )
    assert departures
    for departure in departures:
        assert departure.line_name == "3"
        assert departure.platform == "NSR:Quay:10948"
        assert "3  -> Mortensrud" in str(departure)


def test_get_situations() -> None:  # noqa: D103
    # Test without specifying line_ids
    situations = avgangstider.get_situations(line_ids=[])
    assert situations == []

    # Test with an invalid line number
    situations = avgangstider.get_situations(line_ids=["RUT:Line:0"])
    assert situations == []


@mock.patch("avgangstider.entur_api.entur_query")
def test_get_situations_mocked(  # noqa: D103
    entur_query: Callable[[str, int], str],
    saved_situations_json: dict[str, list[dict[str, str]]],
    saved_situations_list: list[Situation],
    fixed_datetime: type[FixedDateTime],
) -> None:
    # Fake datetime.now() and the situation-json
    entur_query.journey_planner_api().json.return_value = saved_situations_json  # type: ignore
    entur_api.datetime = fixed_datetime("2019-09-21T12:00:00+02:00")  # type: ignore

    # Compared returned situations with the saved result
    situations = avgangstider.get_situations(
        ["RUT:Line:11", "RUT:Line:11", "RUT:Line:35"]
    )
    assert situations == saved_situations_list
    assert str(situations[0]) == str(saved_situations_list[0])
