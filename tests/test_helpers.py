import pytest
from helpers import from_coords_to_int, from_int_to_coords


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ([(0, 0)], 111000000),
        ([(1, 2), (3, 4)], 111001002003004),
        ([(123, 456)], 111123456),
        ([(0, 0), (999, 999)], 111000000999999),
        ([(12, 34), (56, 78), (90, 12)], 111012034056078090012),
    ],
)
def test_from_coords_to_int(input_value, expected_output):
    assert from_coords_to_int(input_value) == expected_output


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (111000000, [(0, 0)]),
        (111001002003004, [(1, 2), (3, 4)]),
        (111123456, [(123, 456)]),
        (111000000999999, [(0, 0), (999, 999)]),
        (111012034056078090012, [(12, 34), (56, 78), (90, 12)]),
    ],
)
def test_from_int_to_coords(input_value, expected_output):
    assert from_int_to_coords(input_value) == expected_output


if __name__ == "__main__":
    pytest.main()
