import pytest
import sys
from rover import Rover
from map import Map


def test_command_validation():

    validMap = Map("unbounded", None)
    test_rover = Rover(100, 100, "east", validMap)

    with pytest.raises(Exception) as excinfo:
        com1 = 10
        test_rover.move(com1)
    assert str(excinfo.value) == "command list is not valid"

    with pytest.raises(Exception) as excinfo:
        com1 = "LRBFx"
        test_rover.move(com1)
    assert str(excinfo.value) == "command list contains invalid commands"

    with pytest.raises(Exception) as excinfo:
        com1 = "LRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBF" \
               "LRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBF" \
               "LRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBFLRBF"
        test_rover.move(com1)
    assert str(excinfo.value) == "list of commands should be less than 100"
