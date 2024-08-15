import random
import math
import time
import numpy
from itertools import repeat
from collections import Counter, OrderedDict

def main():
    print("Rolling for Graveler paralysis, please hold")
    rolls = 0
    highestNumberOfOnes = 0

    # Tracking start time
    startTime = time.time()
    
    # Change this to change size of the array, please limit to 1 million (1000000)
    arraySize = 1000

    # Total number of times to create the random 2d array for calculation.
    # arraySize x numberOfRuns = total number of rolls you finally perform
    numberOfRuns = 1000000

    for x in range(numberOfRuns):

        # Using vectorization to generate a 2d array of numbers given number of attempts and the 231 number of turns.
        # This is extremely fast...but takes a lot of memory, requiring a for loop to assist in doing 1 billion attempts
        vectorizedRandom = numpy.random.randint(1, 5, size=(arraySize, 231)).tolist() 

        for data in vectorizedRandom:
            numberOfOnes = data.count(1)
            rolls = rolls +1
            if numberOfOnes > highestNumberOfOnes:
                highestNumberOfOnes = numberOfOnes
            if highestNumberOfOnes >= 177: # If the number rolled is over 177, break and we stick with the number of rolls taken and no more checks are necessary
                break
    
    # Tracking end time
    endTime = time.time()
    # Calculating final time taken in seconds
    timeTake = endTime-startTime

    # As a side note, it took me personally on my machine 6.662 seconds to calculate 1 million rolls this way

    print("Highest number of ones: ", highestNumberOfOnes)
    print("Number of rolls taken: ", rolls)
    print("Time taken in seconds: ", timeTake)

main()
