# File: player.py
# Authors: Christopher Plummer, ...
# Date: 09/05/2020
# Hackathon 2020
# Description: Contains the classes for each game challenge
# The content of this file implements the code for a cache simulator program


class Player:

    points = 0
    title = ""

    # Constructor
    def __init__(self):
        self.points = 0
        self.title = ""

    # Display points in terminal
    def getPoints(self):
        print("Points: "+self.points)
        return self.points

    # Called after every challenge to set points based on that challenge
    def addPoints(self, p):
        self.points = self.points + p

    # Used at end of game to calculate your title based on points
    def calculateTitle(self):
        if self.points >= 46:
            title = "Cyber Expert"
        elif self.points >= 36:
            title = "Advanced Detective"
        elif self.points >= 30:
            title = "Intermediate Detective"
        elif self.points >= 20:
            title = "Cyber Novice"
        else:
            title = "Flunkie"

        return title
