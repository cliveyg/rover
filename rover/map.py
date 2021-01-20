import settings
import sys


class Map():

    """
    sets map size and map type

      map size is size of the grid - assumes map is square
      map type is the type of map:
        - unbounded: endless plain
        - planet: can go off edge of map and reappear on other side
        - bounded: map has borders - rover cannot go beyond edge of map
    """

    def __init__(self, in_type, size):

        if not isinstance(in_type, str):
            raise Exception("map type is not string")

        map_type = in_type.lower()

        if map_type not in settings.VALID_MAPS:
            raise Exception("map type is not valid")

        self.type = map_type

        # should probably emit a warning about size if map is unbounded
        if self.type == "unbounded":
            self.size = None
        else:
            if not isinstance(size, int):
                raise Exception("size is not an integer")

            if size > sys.maxsize - 1:
                raise Exception("size of map is too big")

            if size < 3:
                raise Exception("map size must be at least 3x3")
            self.size = size
