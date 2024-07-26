import pytest
from base62 import int_to_base62, base62_to_int


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        (0, "0"),
        (1, "1"),
        (61, "z"),
        (62, "10"),
        (12345, "3D7"),
        (999999999, "15ftgF"),
        (12345678901234567890, "EhzL6HwZ5ow"),
    ],
)
def test_int_to_base62(input_value, expected_output):
    assert int_to_base62(input_value) == expected_output


@pytest.mark.parametrize(
    "input_value, expected_output",
    [
        ("0", 0),
        ("1", 1),
        ("z", 61),
        ("10", 62),
        ("3d7", 13957),
        ("GJDGX", 241000605),
        ("1LY7VKfQql", 18242389967325703),
    ],
)
def test_base62_to_int(input_value, expected_output):
    assert base62_to_int(input_value) == expected_output


if __name__ == "__main__":
    pytest.main()
