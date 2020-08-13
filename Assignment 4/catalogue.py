# Assignment 4: Country Classes
"""
This is the file that will create a class that will hold information about
a list of countries.
"""

from country import Country

class CountryCatalogue:
    def __init__(self, firstFile="", secondFile=""):
        # Collection of countries
        self._countryCat = []
        # Dictionary where the key is the country name and the value is the
        # name of the continent
        self._cDictionary = {}

        # Second file deals with information about each country and continent
        # information - continent.txt
        # Use the second file to store the country's name as the key and the
        # country's continent as the value
        try:
            continentInfo = open(secondFile, "r", encoding="utf-8")
            with continentInfo as line:
                # Skip the first line as it's considered the header
                next(line)
                for l in line:
                    countryCont = l.rstrip("\n").split(",")
                    self._cDictionary[countryCont[0]] = countryCont[1]
            continentInfo.close()
        except IOError:
            print("File doesn't exist.")

        # First file deals with information about each country - data.txt
        try:
            countryInfo = open(firstFile, "r", encoding="utf-8")
            with countryInfo as line:
                next(line)
                for l in line:
                    country = l.rstrip("\n").split("|")
                    self._countryCat.append(
                        Country(country[0], int(country[1].replace(',', '')),
                                float(country[2].replace(',', '')),
                                self._cDictionary[country[0]]))
            countryInfo.close()
        except IOError:
            print("File doesn't exist.")

    # findCountry method allows the user to look up information about a
    # certain country
    def findCountry(self, name):
        for n in self._countryCat:
            if n.getName() == name:
                return n

    # setPopulationOfCountry method allows the user to set the population of
    # a country that exists
    def setPopulationOfCountry(self, name, pop):
        for p in self._countryCat:
            if p.getName() == name:
                p.setPopulation(pop)
                return True
        return False

    # setAreaOfCountry method allows the user to set the area of a country
    # that exists
    def setAreaOfCountry(self, name, area):
        for a in self._countryCat:
            if a.getName() == name:
                a.setArea(area)
                return True
        return False

    # addCountry method allows the user to add a new country
    def addCountry(self, name, population, area, continent):
        countryExists = False
        # Checks to see if the country already exists
        for c in self._countryCat:
            if c.getName() == name:
                countryExists = True
        if countryExists == False:
            # The try except block is used to see if the area and population
            # can be converted to a float
            try:
                float(area)
                float(population)
                if str(name).isalpha() and str(
                        continent).isalpha():
                    self._countryCat.append(Country(name, int(population),
                                                    float(area),
                                                    continent))
                    self._cDictionary[name] = continent
                    return True
            except ValueError:
                return False
        return False

    # deleteCountry method allows the user to delete a country from the
    # catalogue and from cDictionary
    def deleteCountry(self, name):
        for c in self._countryCat:
            if c.getName() == name:
                self._countryCat.remove(c)
                self._cDictionary.pop(c.getName())

    # printCountryCatalogue method displays the whole all the countries and
    # their information on the screen
    def printCountryCatalogue(self):
        for c in self._countryCat:
            print(c)

    # getCountriesByContinent method returns a list of countries countries on
    # a specific continent that exists
    def getCountriesByContinent(self, continent):
        sameContinent = []
        for c in self._countryCat:
            if c.getContinent() == continent:
                sameContinent.append(c)
        return sameContinent

    # getCountriesByPopulation method returns a list of countries with their
    # population
    def getCountriesByPopulation(self, continent=""):
        countryAndPop = []
        for c in self._countryCat:
            if c.getContinent() == continent:
                countryAndPop.append((c.getName(), c.getPopulation()))
            elif continent == "":
                countryAndPop.append((c.getName(), c.getPopulation()))
        # lambda is anonymous function. Takes a callable as a parameter
        # usually the key keyword parameter.
        # The negative sign for x will put the large numbers first
        countryAndPop = sorted(countryAndPop, key=lambda x: (-x[1], x[0]))
        return countryAndPop

    # getCountriesByArea method returns a list of countries with their area
    def getCountriesByArea(self, continent=""):
        countryAndArea = []
        for c in self._countryCat:
            if c.getContinent() == continent:
                countryAndArea.append((c.getName(), c.getArea()))
            elif continent == "":
                countryAndArea.append((c.getName(), c.getArea()))
        countryAndArea = sorted(countryAndArea, key=lambda x: (-x[1], x[0]))
        return countryAndArea

    # findMostPopulousContinent method find the most popular continent
    def findMostPopulousContinent(self):
        listOfContinents = {}
        for c in self._countryCat:
            if c.getContinent() not in listOfContinents:
                listOfContinents[c.getContinent()] = 0
            if c.getContinent() in listOfContinents:
                listOfContinents[c.getContinent()] += c.getPopulation()
        # The max function will find the continent with the highest population
        mostPopularCont = max(listOfContinents, key=listOfContinents.get)
        return (mostPopularCont, listOfContinents[mostPopularCont])

    # filterCountriesByPopDensity method will find a list of countries with a
    # population density in between a certain boundary
    def filterCountriesByPopDensity(self, lowerBound, upperBound):
        popDens = []
        for c in self._countryCat:
            if c.getPopDensity() >= lowerBound and c.getPopDensity() <= \
                    upperBound:
                popDens.append((c.getName(), c.getPopDensity()))
        popDens = sorted(popDens, key=lambda x: (-x[1], x[0]))
        return popDens

    # saveCountryCatalogue method allows all the country information to be
    # saved to a file
    def saveCountryCatalogue(self, fileName):
        numIteams = 0
        alphabeticalCountries = []
        try:
            file = open(fileName, "w")
            file.write(
                "Name|Continent|Population|Area Size|Population Density\n")
            for i in self._countryCat:
                alphabeticalCountries.append([i.getName(), i.getContinent(),
                                              i.getPopulation(), i.getArea(),
                                              i.getPopDensity()])
            alphabeticalCountries.sort(key=lambda x: x[0])
            for c in range(0, len(alphabeticalCountries)):
                file.write(alphabeticalCountries[c][0] + "|" +
                           alphabeticalCountries[c][1] + "|" +
                           str(alphabeticalCountries[c][2]) + "|" +
                           str(alphabeticalCountries[c][3]) + "|" +
                           str(alphabeticalCountries[c][4]) + "\n")
                numIteams += 1
            file.close()
        except Exception:
            return -1
        return numIteams
