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
        self.points = 10
        self.title = ""

    # Display points in terminal
    def getpoints(self):
        print("Points: "+self.points)
        return self.points

    # Called after every challenge to set points based on that challenge
    def setpoints(self, p):
        self.points = self.points + p

    # Used at end of game to calculate your title based on points
    def calculatetitle(self):
        if self.points >= 90:
            title = "Cyber Expert"
        elif self.points >= 80:
            title = "Advanced Detective"
        elif self.points >= 70:
            title = "Intermediate Detective"
        elif self.points >= 60:
            title = "Cyber Novice"
        else:
            title = "Flunkie"
