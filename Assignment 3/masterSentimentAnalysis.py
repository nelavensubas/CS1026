# Assignment 3: Sentiment Analysis
"""
This is the module that analyzes Twitter information to perform sentiment
analysis on Twitter data.
"""

# Initialize Constants
PUNC = ".,:;'\"?!#-_[](){}<>\/@$%^&*+=~`|:"

# Create lists
regions = None

def latitudeLongitude(timezone):
    latsLongs = timezone.split(", ")
    # Latitude value
    latsLongs[0] = float(latsLongs[0])
    # Longitude value
    latsLongs[1] = abs(float(latsLongs[1]))
    if latsLongs[0] <= 49.189787 and latsLongs[0] >= 24.660845:
        if latsLongs[1] <= 87.518395 and latsLongs[1] >= 67.444574:
            return "Eastern"
        elif latsLongs[1] <= 101.998892 and latsLongs[1] > 87.518395:
            return "Central"
        elif latsLongs[1] <= 115.236428 and latsLongs[1] > 101.998892:
            return "Mountain"
        elif latsLongs[1] <= 125.242264 and latsLongs[1] > 115.236428:
            return "Pacific"


def removePunc(word):
    newWord = ""
    for c in word:
        if c not in PUNC:
            newWord += c
    return newWord


def compute_tweets(fileTweets, fileKeywords):
    try:
        tweets = open(fileTweets, "r", encoding="utf-8")
        try:
            userTweets = []
            keyWordVals = []
            countedTweets = []

            scoreEastern = 0
            eastern = 0
            scoreCentral = 0
            central = 0
            scoreMountain = 0
            mountain = 0
            scorePacific = 0
            pacific = 0

            easternTZ = 0
            centralTZ = 0
            mountainTZ = 0
            pacificTZ = 0

            regionScores = []

            keywords = open(fileKeywords, "r", encoding="utf-8")
            # This for loop goes through each line in the text file
            for line in tweets:
                # Splits the line into two - first part has the latitude and
                # longitude, second part has the rest of the line
                words = line.split("] ")
                # Remove "[" from the left side of the first part of the line.
                # Now you have you the latitude and longitude separated by comma
                words[0] = words[0].lstrip("[")
                words[0] = latitudeLongitude(words[0])
                # Remove the first 22 characters of the second part of the line
                # because it's irrelevant. Remove the newline character at the
                # end of the second part. Now you only have the tweet
                words[1] = words[1][22:].rstrip("\n")
                words[1] = removePunc(words[1].lower())
                # Add the tweet to a list of tweets
                userTweets.append([words[0], words[1]])

            # This for loop goes through each line in the keywords file
            for line in keywords:
                # Split each line into two parts based on comma
                values = line.split(",")
                if len(values) != 2:
                    print("The files you have entered cannot make the correct "
                          "computations.")
                    print(
                        "Make sure the first file contains the tweets and the "
                        "second file contains the keywords.")
                    exit()
                # Remove the newline character at the end of the second part
                values[1] = values[1].rstrip("\n")
                # Add the keyword and it's associated value to the two
                # dimmensional list
                keyWordVals.append([values[0], values[1]])

            y = 0
            # This for loop goes through all the tweets
            while y < len(userTweets):
                # Make a list of words in the tweet
                tweet = userTweets[y][1].split()
                # row is a sentimental value
                rows = 0
                count = 0
                average = 0
                # Go through each word in the tweet
                for word in tweet:
                    # This while loop will go through the keywords list to see if
                    # one of the keywords match a word in the tweet
                    while rows < len(keyWordVals):
                        if word == keyWordVals[rows][0]:
                            count += 1
                            average += int(keyWordVals[rows][1])
                        rows += 1
                    rows = 0
                # The tweet only matters if it contains a keyword
                if count != 0 and userTweets[y][0] != None:
                    average = float(average / count)
                    countedTweets.append([userTweets[y][0], userTweets[y][
                        1], average, count])
                y += 1

            for t in range(0, len(countedTweets)):
                if countedTweets[t][0] == "Eastern":
                    scoreEastern += countedTweets[t][2]
                    eastern += 1
                elif countedTweets[t][0] == "Central":
                    scoreCentral += countedTweets[t][2]
                    central += 1
                elif countedTweets[t][0] == "Mountain":
                    scoreMountain += countedTweets[t][2]
                    mountain += 1
                elif countedTweets[t][0] == "Pacific":
                    scorePacific += countedTweets[t][2]
                    pacific += 1

            easternTZ = happyScoreTimeZone(easternTZ, scoreEastern, eastern)
            centralTZ = happyScoreTimeZone(centralTZ, scoreCentral, central)
            mountainTZ = happyScoreTimeZone(mountainTZ, scoreMountain, mountain)
            pacificTZ = happyScoreTimeZone(pacificTZ, scorePacific, pacific)

            regionScores.append(easternTZ)
            regionScores.append(centralTZ)
            regionScores.append(mountainTZ)
            regionScores.append(pacificTZ)

            tweets.close()
            keywords.close()

            return regionScores
        except IOError:
            print("%s file does not exist." % fileKeywords)
            regions = None
            return regions
        except ValueError:
            print("The files you have entered cannot make the correct "
                  "computations.")
            print("Make sure the first file contains the tweets and the "
                  "second file contains the keywords.")
            regions = None
            return regions
    except IOError:
        print("%s file does not exist." % fileTweets)
        regions = None
        return regions

def happyScoreTimeZone(timezone, average, count):
    if count == 0:
        timezone = (0, 0)
        return timezone
    else:
        timezone = (round((average / count), 2), count)
        return timezone
