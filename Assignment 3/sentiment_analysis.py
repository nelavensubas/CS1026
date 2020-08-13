# Assignment 3: Sentiment Analysis
"""
This is the module that analyzes Twitter information to perform sentiment
analysis on Twitter data.
"""

# Initialize Constants
PUNC = ".,:;'\"?!#-_[](){}<>\/@$%^&*+=~`|:"

# Create lists
regions = None

## Figure out the timezone the tweet is from.
# @param timezone The latitude and longitude values of the tweet
# @return the timezone the tweet is from
#
def latitudeLongitude(timezone):
    latsLongs = timezone.split(", ")
    latsLongs[0] = float(latsLongs[0])  # Latitude value
    latsLongs[1] = abs(float(latsLongs[1]))  # Longitude value
    # This if statement and the following nested if statement will determine
    # which timezone the tweet is from
    if latsLongs[0] <= 49.189787 and latsLongs[0] >= 24.660845:
        if latsLongs[1] <= 87.518395 and latsLongs[1] >= 67.444574:
            return "Eastern"
        elif latsLongs[1] <= 101.998892 and latsLongs[1] > 87.518395:
            return "Central"
        elif latsLongs[1] <= 115.236428 and latsLongs[1] > 101.998892:
            return "Mountain"
        elif latsLongs[1] <= 125.242264 and latsLongs[1] > 115.236428:
            return "Pacific"

## Removes all punctuation in a word
# @param word a word that does or does not have punctuation to begin with
# @return a new word that has no punctuation
#
def removePunc(word):
    newWord = ""
    # This for loop will go through each character in the word and check to
    # see if it's a punctuation or not. If it is, don't add it to the new word.
    for c in word:
        if c not in PUNC:
            newWord += c
    return newWord

## Process the tweets and keywords to determine the happiness score for each
# timezone
# @param fileTweets the file that contains all the tweets to be analyzed
# @param fileKeywords the file that contains all the keywords
# @return a list that contains the happiness score and the amount of valid
# tweets for each timezone
#
def compute_tweets(fileTweets, fileKeywords):
    # The next two while loops are used to make sure the user has entered a
    # file name that exists
    while True:
        try:
            tweets = open(fileTweets, "r", encoding="utf-8")
            break
        except IOError:
            print("\nThe file name \"%s\" does not exist." % fileTweets)
            fileTweets = input("Enter the name of the tweets file: ")

    while True:
        try:
            keywords = open(fileKeywords, "r", encoding="utf-8")
            break
        except IOError:
            print("\nThe file name \"%s\" does not exist." % fileKeywords)
            fileKeywords = input("Enter the name of the keywords file: ")

    # This try block will try to make computations in order to determine the
    # hapiness score for each tweet and the overall happiness score for each
    # timezone.
    try:
        # A two-dimensional list that will contain the timezone and tweet
        userTweets = []
        # A two-dimensional list that will contain the keywords and its values
        keyWordVals = []
        # A two-dimensional list that will contain the all the valid tweets
        # with its timezone, tweet, overall happiness score and the amount of
        # keywords found in the tweet
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

        # A list of tuples that will have the overall happiness score and the
        # amount of valid tweets for each timezone
        regionScores = []

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
            # Add the tweet and timezone to a list
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

        # Create a sentinel value
        y = 0
        # This for loop goes through all the tweets
        while y < len(userTweets):
            # Make a list of words in the tweet
            tweet = userTweets[y][1].split()
            # row is a sentinel value
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
            # The tweet only matters if it contains a keyword and the tweet
            # is from either the Eastern, Central, Mountain, or Pacific timezone
            if count != 0 and userTweets[y][0] != None:
                average = float(average / count)
                countedTweets.append([userTweets[y][0], userTweets[y][
                    1], average, count])
            y += 1

        # This for loop goes through each of the valid tweets and add its
        # happiness score to the correct timezone to calculate the overall
        # happiness score for the specific timezone
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

        # Close the tweets and keywords files
        tweets.close()
        keywords.close()

        return regionScores
    # The ValueError exception is used in case there was a problem making the
    # correct calculations
    except ValueError:
        print("\nThe files you have entered cannot make the correct "
              "computations.")
        print("Make sure the first file contains the tweets and the "
              "second file contains the keywords.")
        tweets.close()
        keywords.close()
        return regions

## Figures out the overall happiness score for each timezone and includes the
# amount of valid tweets
# @param timezone the specific timezone: eastern, central, mountain, or pacific
# @param average the sum of happiness scores for each tweet that will be used
# to figure out the overall happiness score
# @param count the amount of valid tweets from that specific timezone
# @return a tuple that contains the overall happiness score and the amount of
# valid tweets
#
def happyScoreTimeZone(timezone, average, count):
    # Checks to see if there were no valid tweets from a certain timezone to
    # avoid a ZeroDivision error
    if count == 0:
        timezone = (0, 0)
        return timezone
    else:
        # round the overall happiness score to two
        timezone = (round((average / count), 2), count)
        return timezone
