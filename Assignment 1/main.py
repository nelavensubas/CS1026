# Assignment 1: Coffee or Tea
"""
This program will ask the customer if he/she wants coffee or tea and computes
the total cost of the beverage.
"""

# Initialize constant variables
SMALL = 1.50
MEDIUM = 2.50
LARGE = 3.25
VANILLA = 0.25
CHOCOLATE = 0.75
LEMON = 0.25
MINT = 0.50

name = ""
beverage = ""
size = ""
flavour = ""
cost = 0

"""
Ask the customer to enter their name. Use .replace() to remove all spaces in
their name.
"""
name = input("Would you please enter your name: ").replace(" ", "")

"""
Ask the customer to enter their choice of beverage. Use .lower() to covert all 
letters into lowercase.
"""
beverage = input("Would you like a cup of coffee or tea: ").lower()
# Check to see if the user chose a cup of coffee or tea
if beverage == "c" or beverage == "coffee" or beverage == "t" or beverage == "tea":
    size = input("What size would you like: ").lower()
    """
    Figure out the size that the customer wants in order to determine how
    much he/she will be charged.
    """
    if size == "s" or size == "small":
        cost += SMALL
        size = "small"
    elif size == "m" or size == "medium":
        cost += MEDIUM
        size = "medium"
    elif size == "l" or size == "large":
        cost += LARGE
        size = "large"
    else:
        print("That size doesn't exist. You can only order a small, medium, "
              "or large.")
        exit()
else:
    print("That beverage doesn't exist. You can only order a cup of coffee or "
          "tea.")
    # exit will terminate the program if the user enters incorrect input
    exit()

# Each beverage has different flavours so we need to check what the user ordered
if beverage == "c" or beverage == "coffee":
    flavour = input("What flavour would you like, vanilla, chocolate, or none "
                    "(enter only one): ").lower()
    """
    Figure out the flavour that the customer chose in order to determine how
    much he/she will be charged.
    """
    if flavour == "v" or flavour == "vanilla":
        cost += VANILLA
        flavour = "vanilla"
    elif flavour == "c" or flavour == "chocolate":
        cost += CHOCOLATE
        flavour = "chocolate"
    elif flavour == "none" or flavour == "":
        flavour = "none"
    else:
        print("That flavour doesn't exist. You can only order one flavour for a cup of "
              "coffee: chocolate, vanilla, or none.")
        exit()
    beverage = "coffee"
# An else if statement will be used if the user ordered tea
elif beverage == "t" or beverage == "tea":
    flavour = input("What flavour would you like, lemon, mint, or none (enter "
                    "only one): ").lower()
    if flavour == "l" or flavour == "lemon":
        cost += LEMON
        flavour = "lemon"
    elif flavour == "m" or flavour == "mint":
        cost += MINT
        flavour = "mint"
    elif flavour == "none" or flavour == "":
        flavour = "none"
    else:
        print("That flavour doesn't exist. You can only order one flavour for a cup of "
              "tea: lemon, mint, or none.")
        exit()
    beverage = "tea"

# Round the final cost with tax included to two decimal places
cost = round(cost * 1.13, 2)

# Display the amount of money billed
if flavour == "none":
    print("For " + name + ", a %s %s" % (size, beverage) + ", no flavoring,",
          "cost: ${:.2f}.".format(cost))
else:
    print("For " + name + ", a %s %s" % (size, beverage) + ", with {},".format(flavour),
          "cost: $%.2f." % cost)
