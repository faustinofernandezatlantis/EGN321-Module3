import pytest
from src.selection_tool import select_coefficient


# Exact lookup tests
def test_exact_lookup_vx100():
    res = select_coefficient("VX-100", 40)
    assert res["coefficient"] == 0.93
    assert res["method"] == "exact"


def test_exact_lookup_vx200():
    res = select_coefficient("VX-200", 50)
    assert res["coefficient"] == 1.27
    assert res["method"] == "exact"


# Interpolation tests
def test_interpolation_vx100():
    res = select_coefficient("VX-100", 30)  # Between 20(0.88) and 40(0.93) -> 0.905
    assert res["coefficient"] == pytest.approx(0.905)
    assert res["method"] == "interpolation"


def test_interpolation_vx200():
    res = select_coefficient("VX-200", 65)  # Between 50(1.27) and 70(1.39) -> 1.36
    assert res["coefficient"] == pytest.approx(1.36)
    assert res["method"] == "interpolation"


# Boundary tests
def test_lower_boundary():
    res = select_coefficient("VX-100", 20)
    assert res["coefficient"] == 0.88


def test_upper_boundary():
    res = select_coefficient("VX-100", 100)
    assert res["coefficient"] == 1.14


# Refusal tests
def test_below_range_refused():
    with pytest.raises(ValueError, match="below the supported minimum"):
        select_coefficient("VX-100", 10)


def test_above_range_refused():
    with pytest.raises(ValueError, match="exceeds the supported maximum"):
        select_coefficient("VX-200", 95)


def test_unsupported_family_refused():
    with pytest.raises(ValueError, match="Unsupported valve_family"):
        select_coefficient("VX-999", 50)