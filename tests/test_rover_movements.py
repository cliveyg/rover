import pytest
import sys
from rover import Rover
from map import Map

def test_current_position():

    validMap = Map("unbounded", None)
    test_rover = Rover(10, 10, "north", validMap)

    assert test_rover.show_current_position() == "(10, 10) NORTH" 


def test_orientations():

    validMap = Map("unbounded", None)
    test_rover = Rover(3, 5, "east", validMap)

    commands = "LL"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(3, 5) WEST"

    commands = "LL"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(3, 5) EAST"

    commands = "RR"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(3, 5) WEST"

    commands = "RR"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(3, 5) EAST"


def test_forwards_and_back():

    validMap = Map("unbounded", None)
    test_rover = Rover(26, 88, "south", validMap)

    commands = "FF"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(26, 86) SOUTH"

    commands = "BBBBB"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(26, 81) SOUTH"


def test_negative_coordinates():

    validMap = Map("unbounded", None)
    test_rover = Rover(-1, -1, "north", validMap)

    commands = "FF"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(-1, 1) NORTH"

    commands = "RFF"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(1, 1) EAST"

    commands = "RFF"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(1, -1) SOUTH"

    commands = "RFF"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(-1, -1) WEST"


    commands = "RFF"
    test_rover.move(commands)

    assert test_rover.show_current_position() == "(-1, 1) NORTH"

