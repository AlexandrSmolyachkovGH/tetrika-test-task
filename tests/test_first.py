import pytest
from contextlib import nullcontext as does_not_raise

from tasks.first import sum_two


# First task
@pytest.mark.parametrize(
    "a, b, c, expectation",
    [
        (1, 2, 3, does_not_raise()),
        (1, "2", 3, pytest.raises(TypeError, match="Wrong attr type")),
        (1, 2.5, 3.5, pytest.raises(TypeError, match="Wrong attr type")),
    ]
)
def test_first_task(a, b, c, expectation):
    with expectation:
        result = sum_two(a, b)
        assert result == c
