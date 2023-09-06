import pytest
from src.subject import get_result


def test_get_result():
    with pytest.raises(ValueError):
        get_result("a")
    with pytest.raises(ValueError):
        get_result("111:11")
    with pytest.raises(ValueError):
        get_result("24:11")
    with pytest.raises(ValueError):
        get_result("21:60")
    with pytest.raises(ValueError):
        get_result("25:00")
    assert get_result("00:00") == 0
    assert get_result("12:00") == 360
    assert get_result("06:00") == 180
    assert get_result("12:30") == 180
    assert get_result("12:45") == 90
    assert get_result("12:36") == 144
    assert get_result("08:00") == 120

