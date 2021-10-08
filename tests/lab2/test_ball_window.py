import numpy as np
import pytest

from lab2.ball_window import BallWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "center, radius, expected",
    [
        ([2.5, 2.5], 1, "A ball with center= [2.5 2.5] and radius= 1"),
        ([0, 5, 4], 3, "A ball with center= [0 5 4] and radius= 3"),
    ],
)
def test_box_string_representation(center, radius, expected):
    assert str(BallWindow(center, radius)) == expected


@pytest.fixture
def ball_1():
    return BallWindow([0, 5], 2)


@pytest.mark.parametrize(
    "point, expected", [([0, 6], True),],
)
def test_contains_ball_1(ball_1, point, expected):
    is_in = ball_1.__contains__(point)
    assert is_in == expected


@pytest.mark.parametrize(
    "center, radius, expected", [([1, 2], 1, "The volume is 4.19"),],
)
def test_ball_volume(center, radius, expected):
    assert (BallWindow(center, radius)).volume() == expected


@pytest.mark.parametrize(
    "center, radius, expected",
    [([1, 2], 1, "The area is 12.57"), ([3, 2, 4], 2, "The area is 50.27"),],
)
def test_ball_area(center, radius, expected):
    assert (BallWindow(center, radius)).area() == expected
