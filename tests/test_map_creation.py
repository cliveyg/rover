import pytest
import sys
from map import Map


def test_map_initialisation():
    with pytest.raises(TypeError):
        test_map = Map()


def test_map_type_not_valid():
    with pytest.raises(Exception) as excinfo:
        test_map = Map("blah", 100)
    assert str(excinfo.value) == "map type is not valid"

    with pytest.raises(Exception) as excinfo:
        test_map = Map(100, 99)
    assert str(excinfo.value) == "map type is not string"


def test_all_valid_map_types():
    test_map1 = Map("Bounded", 100)
    assert test_map1.type == "bounded"
    test_map2 = Map("PLANET", 100)
    assert test_map2.type == "planet"
    test_map3 = Map("unbounded", 100)
    assert test_map3.type == "unbounded"


def test_map_size_exceptions():
    with pytest.raises(Exception) as excinfo:
        test_map = Map("bounded", "blah")
    assert str(excinfo.value) == "size is not an integer"

    with pytest.raises(Exception) as excinfo:
        test_map = Map("planet", 9223372036854775808)
    assert str(excinfo.value) == "size of map is too big"

    with pytest.raises(Exception) as excinfo:
        test_map = Map("planet", -22)
    assert str(excinfo.value) == "map size must be at least 3x3"
