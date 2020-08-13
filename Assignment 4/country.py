# Assignment 4: Country Classes
"""
This is the file that will create a class that will hold information about a
single country.
"""

class Country:
    # The constructor method
    def __init__(self, name, pop, area, continent):
        self._name = name
        self._population = pop
        self._area = area
        self._continent = continent

    # The getter method for getting the country's name
    def getName(self):
        return self._name

    # The getter method for getting the country's population
    def getPopulation(self):
        return self._population

    # The setter method for setting the country's population
    def setPopulation(self, pop):
        self._population = pop

    # The getter method for getting the country's area
    def getArea(self):
        return self._area

    # The setter method for setting the country's area
    def setArea(self, area):
        self._area = round(area, 2)

    # The getter method for getting the country's continent
    def getContinent(self):
        return self._continent

    # The setter method for setting the country's continent
    def setContinent(self, continent):
        self._continent = continent

    # The getter method for getting the country's population density
    def getPopDensity(self):
        return round((self._population / self._area), 2)

    # __repr__(self) generates a string representation in the form of
    # Name(pop: population value, size: area value) in Continent
    def __repr__(self):
        return "%s(pop: %d, size: %.2f) in %s" % (self._name, self._population,
                                                  self._area, self._continent)
