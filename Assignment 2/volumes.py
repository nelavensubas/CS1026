# Assignment 2: Volume Calculator
# This module will compute volumes.

# Import the math module
import math

# Initialize constant variables
PI = math.pi

# Create lists
cubeVolumes = []
pyramidsVolumes = []
ellipsoidsVolumes = []

## Calculate the volume of a cube
# @return the volume of the cube
#
def cube():
    a = int(input("Enter a length: "))

    volume = a ** 3
    print("The volume of a cube with length", a, "is:", volume)

    # Add the volume to the list of cube volumes
    cubeVolumes.append(volume)

    return volume

## Calculate the volume of a pyramid
# @return the volume of the pyramid
#
def pyramid():
    b = float(input("Enter a base: "))
    h = float(input("Enter a height: "))

    # Round the calcuated volume to two decimal places
    volume = round((1 / 3) * (b ** 2) * h, 2)
    print("The volume of a pyramid with base", b, "and height", h, "is: %.2f"
          % volume)

    # Add the volume to the list of pyramid volumes
    pyramidsVolumes.append(volume)

    return volume

## Calculate the volume of an ellipsoid
# @return the volume of the ellipsoid
#
def ellipsoid():
    r1 = float(input("Enter the first radius: "))
    r2 = float(input("Enter the second radius: "))
    r3 = float(input("Enter the third radius: "))

    # Round the calculated volume to two decimal places
    volume = round((4 / 3) * PI * r1 * r2 * r3, 2)
    print("The volume of ellipsoid with its first raidus %d, second radius "
          "%d, and third radius %d is: %.2f" % (r1, r2, r3, volume))

    # Add the volume to the list of ellipsoid volumes
    ellipsoidsVolumes.append(volume)

    return volume
