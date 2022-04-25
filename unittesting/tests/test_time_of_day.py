"""Testing time of day with freeze and mock"""

import datetime
from unittest import mock
from freezegun import freeze_time
from unittesting.to_test import time_of_day


@freeze_time("2022-04-23 14:30:00")
def test_time_afternoon():
    """Check time like afternoon"""
    assert time_of_day() == 'afternoon'
    assert time_of_day() == 'morning'


@freeze_time("2022-04-23 03:14:57")
def test_time_night():
    """Check time like afternoon"""
    assert time_of_day() == 'night'


@freeze_time("2022-04-23 09:19:34")
def test_time_morning():
    """Check time morning"""
    assert time_of_day() == 'morning'


# new time by alternative variant
NEW_DAY = datetime.datetime(year=2020, month=12, day=31, hour=23, minute=55, second=30)


@freeze_time(NEW_DAY)
def test_time_now():
    """Testing by freezetime and mock"""
    assert time_of_day() == 'morning'


class FakeTime(datetime.datetime):
    """Change time for mock"""
    def __new__(cls):
        return datetime.datetime.now.__new__(datetime)


@mock.patch('datetime.date', FakeTime)
def mock_path():
    """Mock time for testing func"""
    FakeTime.now = classmethod(lambda cls: datetime.datetime(2020, 1, 1, 23, 23, 23))
    return FakeTime.now


@freeze_time(mock_path()())
def test_time_by_mock():
    """Testing time with mock custom"""
    assert time_of_day() == 'morning'
