import challenges


class Decryption(challenges.Challenge):
    # Variables
    prompt = "Hello... its your boss ... we have intellegence on the UT Database. Decrypt these emails and we might " \
             "gain a lead on whos been attacking us...We know this is a Caesar Cipher and the key is 5. "
    points = 0
    timeLimit = 5 * 60
    emailsEncrypted = ["qkdqhb1996z@pryr.frp", "ehuqdugp@ahpqh.frp", "ykdoh@pryr.frp", "ehyorqjkruq@jpdlo.frp"]
    emailsAns = ["nhaney1996w@movo.com", "bernardm@xemne.com", "vhale@movo.com", "bevlonghorn@gmail.com"]

    def getPrompt(self):
        return self.prompt

    def getTimeLimit(self):
        return self.timeLimit

    # Use to access emails and display them in main
    def getEmails(self):
        return self.emailsEncrypted

    def getPoints(self):
        return self.points

    def computePoints(self, userResult):
        countCheck = 0
        for x in userResult:
            if x in self.emailsAns:
                self.points += 2
                countCheck += 1

        # Bonus point to equal 10 total
        if countCheck == 4:
            self.points += 1

    # Use this to compare results to user answers, 2 points for correct email
    def getResult(self, userResult):

        self.computePoints(userResult)

        countCheck = 0
        for x in userResult:
            if x in self.emailsAns:
                countCheck += 1

        if countCheck == 4:
            return True
        return False
