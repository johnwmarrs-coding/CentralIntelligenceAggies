# File: challenges.py
# Date: 09/05/2020
# Description: Contains the classes for each game challenge
# The content of this file implements the code for a cache simulator program


class Challenge:
    
    fail = False
    
    # Number of points to give to player
    result = 0

    # Constructor
    def __init__(self):
        self.fail = True
        self.result = 0


# Subclasses in respective files
