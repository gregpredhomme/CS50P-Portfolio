from seasons import get_minutes, format_words
from datetime import date
import pytest

def test_get_minutes():
    start = date(2022, 1, 1)
    end = date(2023, 1, 1)
    assert get_minutes(start, end) == 525600

    start_leap = date(2019, 1, 1)
    end_leap = date(2021, 1, 1)
    assert get_minutes(start_leap, end_leap) == 1052640

def test_format_words():
    assert format_words(525600) == "Five hundred twenty-five thousand, six hundred minutes"
    assert format_words(3298) == "Three thousand, two hundred ninety-eight minutes"
