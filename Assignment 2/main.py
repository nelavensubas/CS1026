# Assignment 2: Volume Calculator
"""
This is the main program, which computes the volume for a number of
different shapes by using the functions from the volume module.
"""

# Import everything from the volumes module.
from volumes import *

# Initialize constant variables
VALIDINPUTS = ["cube", "c", "pyramid", "p", "ellipsoid", "e", "quit", "q"]

# Create a sentinel value
valid = 0

## Checks what the user has entered
# @param userInput the string the user has entered
# @return a valid input
#
def checkInput(userInput):
    while userInput not in VALIDINPUTS:
        # Keeping asking the user to enter something as long as it's valid input
        userInput = input("Sorry, that shape doesnt exist, please enter a "
                          "valid shape: ").lower()
    return userInput

## Display the list of volumes for each shape from lowest to highest order
# @param selectedShape the name of the shape
# @param shapeName the list with all the volumes for the specific shape
# @return display the volumes calculated from least to greatest for the specific shape
#
def displayLists(selectedShape, shapeName):
    # shapeName length would be zero if no calculations were performed for
    # that shape
    if len(shapeName) == 0:
        return selectedShape + ": No shapes entered"
    else:
        # sort() will sort the values in the list from least to greatest
        shapeName.sort()
        volumes = selectedShape + ": "
        # This for loop will be used to print all the volumes from the
        # specific shape on one line
        for i in range(0, len(shapeName)):
            if i == len(shapeName) - 1:
                volumes += str(shapeName[i])
            else:
                volumes += str(shapeName[i]) + ", "
        return volumes

shape = input("Please enter a shape: ").lower()
shape = checkInput(shape)

'''
Use this while loop to figure out how many times each shape needs to be 
calculated and to continue asking the user for valid input.
'''
while valid == 0:
    if shape == "cube" or shape == "c":
        cube()
        shape = input("\nPlease enter a shape: ").lower()
        shape = checkInput(shape)
    elif shape == "pyramid" or shape == "p":
        pyramid()
        shape = input("\nPlease enter a shape: ").lower()
        shape = checkInput(shape)
    elif shape == "ellipsoid" or shape == "e":
        ellipsoid()
        shape = input("\nPlease enter a shape: ").lower()
        shape = checkInput(shape)
    elif shape == "quit" or shape == "q":
        valid = 1

"""
Tell the user the session has ended and display all the volume calculations 
if there are any.
"""
if len(cubeVolumes) == 0 and len(pyramidsVolumes) == 0 and len(ellipsoidsVolumes) == 0:
    print("\nYou have reached the end of your session.\nYou did not perform any "
          "volume calculations.")
else:
    print("\nYou have reached the end of your session.")
    print("The volumes calculated for each shape are:")

    print(displayLists("Cube", cubeVolumes))
    print(displayLists("Pyramid", pyramidsVolumes))
    print(displayLists("Ellipsoid", ellipsoidsVolumes))
