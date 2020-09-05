# File: challenges.py
# Authors: Christopher Plummer, ...
# Date: 09/05/2020
# Hackathon 2020
# Description: Contains the classes for each game challenge
# The content of this file implements the code for a cache simulator program


class Challenge:
    # Set true of player passes the challenge
    fail = False

    # Number of points to give to player
    result = 0

    # Constructor
    def __init__(self):
        self.fail = False
        self.result = 0


# Inherited or Sub class (Note Person in bracket)

class EncriptionChallenge(Challenge):
    def runencript(self):
        print("### Encription Challenge ###")


class DDOSChallenge(Challenge):
    def runddos(self):
        print("### DDOS Challenge ###")


class MalwareChallenge(Challenge):
    def runmalware(self):
        print("### Malware Challenge ###")


class PhishingChallenge(Challenge):
    def runphish(self):
        print("### Phising Challenge ###")


class PasswordChallenge(Challenge):
    def runpassword(self):
        print("### Password security Challenge ###")


class DecryptChallenge(Challenge):
    def runsqlinject(self):
        print("### Decrypt Challenge ###")


class SQLChallenge(Challenge):
    def runsqlinject(self):
        print("### SQL Injection Challenge ###")


class RansomChallenge(Challenge):
    def runransom(self):
        print("### Ransom Challenge ###")


class ManInMiddleChallenge(Challenge):
    def runmaninmid(self):
        print("### Man in Middle Challenge ###")
