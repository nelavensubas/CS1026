# Assignment 3: Sentiment Analysis
"""
This is the main program, that uses the sentiment_analysis module to analyze
Twitter information.
"""

# Import everything from the sentiment_analysis module
from sentiment_analysis import *

# Create and initialize variables
highestScore = 0
happiest = 0

# Get input from the user on which tweets file and keywords file to use
userTweets = input("Enter the name of the tweets file: ")
userKeywords = input("Enter the name of the keywords file: ")

# Call the function compute_tweets and store the results
regions = compute_tweets(userTweets, userKeywords)

# Check to see if an empty list was returned. If not, show the happiness
# score for each timezone.
if regions != None:
    print("\nThe Eastern timezone happiness score:", regions[0][0])
    print("The Central timezone happiness score:", regions[1][0])
    print("The Mountain timezone happiness score:", regions[2][0])
    print("The Pacific timezone happiness score:", regions[3][0])

    # Use this for loop to figure out which timezone has the highest
    # happiness score.
    for r in range(0, 4):
        if regions[r][0] > highestScore:
            highestScore = regions[r][0]
            happiest = r

    if happiest == 0:
        print("Therefore, the happiest timezone is Eastern.")
    elif happiest == 1:
        print("Therefore, the happiest timezone is Central.")
    elif happiest == 2:
        print("Therefore, the happiest timezone is Mountain.")
    elif happiest == 3:
        print("Therefore, the happiest timezone is Pacific.")
