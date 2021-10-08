import numpy as np
import pytest

from sdia_python.lab2.box_window import BoxWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), "BoxWindow: [2.5, 2.5]"),
        (np.array([[0, 5], [0, 5]]), "BoxWindow: [0, 5] x [0, 5]"),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
            "BoxWindow: [0.0, 5.0] x [-1.45, 3.14] x [-10.0, 10.0]",
        ),
    ],
)
def test_box_string_representation(bounds, expected):
    assert str(BoxWindow(bounds)) == expected

    # ================================
    # ==== WRITE YOUR TESTS BELOW ====
    # ================================

    # @pytest.mark.parametrize(
    "bounds, expected", [([[3, 2]], AssertionError),],


# )
# def test_bounds(bounds, expected):
# assert BoxWindow(bounds) == expected


@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_indicator_function_box_2d(box_2d_05, point, expected):
    is_in = box_2d_05.indicator_function(point)
    assert is_in == expected


@pytest.mark.parametrize(
    "listofpoint, expected",
    [(np.array([[0, 0], [2.5, 2.5], [-1, 5], [10, 3]]), [True, True, False, False]),],
)
def test_indicator_function_several_box_2d(box_2d_05, listofpoint, expected):
    is_in = box_2d_05.indicator_function_several(listofpoint)
    assert is_in == expected


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_contains_box_2d(box_2d_05, point, expected):
    is_in = box_2d_05.__contains__(point)
    assert is_in == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), 0),
        (np.array([[0, 20], [-10, -6], [-5, 5]]), 800),
        (np.array([[0, 0], [0, 0], [-10, 10]]), 0),
    ],
)
def test_box_volume(bounds, expected):
    assert BoxWindow(bounds).volume() == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), [2.5]),
        (np.array([[0, 20], [-10, -6], [-5, 5]]), [10, -8, 0]),
        (np.array([[0, 0], [0, 0], [-10, 10]]), [0, 0, 0]),
    ],
)
def test_box_center(bounds, expected):
    assert BoxWindow(bounds).center() == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), [0]),
        (np.array([[0, 20], [-10, -6], [-5, 5]]), [20, 4, 10]),
        (np.array([[0, 0], [0, 0], [-10, 10]]), [0, 0, 20]),
    ],
)
def test_length(bounds, expected):
    assert BoxWindow(bounds).length() == expected


def test_rand_box_2d_05(box_2d_05):
    assert np.all(box_2d_05.indicator_function_several(box_2d_05.rand(n=10)))
