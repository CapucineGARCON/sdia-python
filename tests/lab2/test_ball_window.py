import numpy as np
import pytest

from lab2.ball_window import BallWindow, UnitBallWindow


def test_raise_type_error_when_radius_invalid():
    with pytest.raises(AssertionError):
        BallWindow([2, 1], -10)


def test_raise_type_error_when_center_invalid():
    with pytest.raises(AssertionError):
        BallWindow([], 2)


def test_raise_type_error_when_point_dimension_invalid():
    with pytest.raises(AssertionError):
        ball = BallWindow([1, 2, 3], 2)
        ball.__contains__([1, 2])


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


@pytest.mark.parametrize(
    "points, expected",
    [([[0, 6], [0, 2], [0, 0], [1, 4.5]], [True, False, False, True]),],
)
def test_indicator_function_ball_1(ball_1, points, expected):
    assert ball_1.indicator_function(points) == expected


@pytest.mark.parametrize(
    "center, radius, expected",
    [([0, 6], 2, 2), ([1, 2, 3], 6, 3), ([10, 0, 9, 1], 1, 4),],
)
def test_ball_dimension(center, radius, expected):
    assert BallWindow(center, radius).dimension() == expected


@pytest.mark.parametrize(
    "center, expected", [([0, 6], 1), ([1, 2, 3], 1), ([10, 0, 9, 1], 1),],
)
def test_Unit_Ball(center, expected):
    assert UnitBallWindow(center).radius == expected
