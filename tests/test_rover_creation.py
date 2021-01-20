import pytest
import sys
from map import Map
from rover import Rover


def test_rover_initialisation():
    with pytest.raises(TypeError):
        test_map = Rover()


def test_rover_initialisation_not_valid():

    validMap = Map("planet", 100)

    with pytest.raises(Exception) as excinfo:
        test_rover1 = Rover("e", 100, "EAST", validMap)
    assert str(excinfo.value) == "x co-ordinate is not an integer"

    with pytest.raises(Exception) as excinfo:
        test_rover2 = Rover(100, "e", "EAST", validMap)
    assert str(excinfo.value) == "y co-ordinate is not an integer"

    with pytest.raises(Exception) as excinfo:
        test_rover3 = Rover(100, 99, 33, validMap)
    assert str(excinfo.value) == "direction is not a string"

    with pytest.raises(Exception) as excinfo:
        test_rover3 = Rover(100, 99, "beast", validMap)
    assert str(excinfo.value) == "direction is not a valid value"

    with pytest.raises(Exception) as excinfo:
        test_rover4 = Rover(100, 99, "East", "something")
    assert str(excinfo.value) == "map is not valid"


def test_all_valid_directions():

    validMap = Map("planet", 100)

    test_east = Rover(100, 100, "east", validMap)
    assert test_east.direction == "EAST"

    test_east = Rover(100, 100, "West", validMap)
    assert test_east.direction == "WEST"

    test_east = Rover(100, 100, "nOrTH", validMap)
    assert test_east.direction == "NORTH"

    test_east = Rover(100, 100, "SOUTH", validMap)
    assert test_east.direction == "SOUTH"
