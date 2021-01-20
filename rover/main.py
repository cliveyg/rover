import sys
import os
from map import Map
from rover import Rover

def main():

    print("Input x y D where x and y are integers and D is north, south, " \
          "east or west\n")
    while True:
        input_vars = input("Please enter rovers initial co-ordinates in " \
                           "the format x y D: ")

        input_array = input_vars.split()
        if len(input_array) != 3:
            print("Ypu need to enter three values")
        else:
            try:
                x = int(input_array[0])
                y = int(input_array[1])
            except:
                print("x and/or y are not valid integers")
                print("Try again\n") 
            else:
                try:
                    default_map = Map("unbounded", None)
                    direction = input_array[2]
                    rover = Rover(x, y, direction, default_map)
                except Exception as e:
                    print(e)
                    print("Try again\n")
                else:
                    print("Rover is currently at co-ordinates: "+ 
                           rover.show_current_position())

                    print("Please enter a list of commands. Valid commands are " \
                          "L R B F for left, right, back and forward")

                    while True:
                        commands = input("Enter commands with no spaces: ")
                        try:
                            rover.move(commands)
                        except Exception as e:
                            print(e)
                            print("Try again\n")
                        else:
                            print("Rover is currently at co-ordinates: "+ 
                                  rover.show_current_position())
                            print("Enter some more commands:\n")
    

if __name__ == '__main__':
	main()
