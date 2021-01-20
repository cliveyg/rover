import sys
from map import Map
import settings
import re


class Rover():

    # rotate directions is easiest way to calculate l and r
    orientate_left = {
        "NORTH": "WEST",
        "WEST": "SOUTH",
        "SOUTH": "EAST",
        "EAST": "NORTH"
    }

    orientate_right = {
        "NORTH": "EAST",
        "EAST": "SOUTH",
        "SOUTH": "WEST",
        "WEST": "NORTH"
    }

    def __init__(self, x, y, indir, in_map):

        if not isinstance(x, int):
            raise Exception("x co-ordinate is not an integer")

        if not isinstance(y, int):
            raise Exception("y co-ordinate is not an integer")

        if not isinstance(indir, str):
            raise Exception("direction is not a string")

        direction = indir.upper()
        if direction not in settings.VALID_DIRECTIONS:
            raise Exception("direction is not a valid value")

        if not isinstance(in_map, Map):
            raise Exception("map is not valid")

        self.x = x
        self.y = y
        self.direction = direction
        self.map = in_map

    def move(self, commands):

        try:
            self.__check_command_list(commands)
        except Exception:
            raise

        self.__calculate_position(commands)
        self.show_current_position()

    def show_current_position(self):

        position = "(%d, %d) %s" % (self.x, self.y, self.direction)
        return position

    def __calculate_position(self, commands):

        for cmd in list(commands):

            if cmd == "F":
                if self.direction == 'NORTH':
                    self.y = self.y + 1
                elif self.direction == 'EAST':
                    self.x = self.x + 1
                elif self.direction == 'SOUTH':
                    self.y = self.y - 1
                elif self.direction == 'WEST':
                    self.x = self.x - 1

            if cmd == "B":
                if self.direction == 'NORTH':
                    self.y = self.y - 1
                elif self.direction == 'EAST':
                    self.x = self.x - 1
                elif self.direction == 'SOUTH':
                    self.y = self.y - 1
                elif self.direction == 'WEST':
                    self.x = self.x + 1

            if cmd == "L":
                self.direction = self.orientate_left[self.direction]
            elif cmd == "R":
                self.direction = self.orientate_right[self.direction]

    def __check_command_list(self, in_comms):

        if not isinstance(in_comms, str):
            raise Exception("command list is not valid")
        if len(in_comms) > 100:
            raise Exception("list of commands should be less than 100")

        commands = in_comms.upper()

        regex_string = "^[%s]+$" % (settings.VALID_COMMANDS)
        reg = re.compile(regex_string)

        if not reg.match(commands):
            raise Exception("command list contains invalid commands")
