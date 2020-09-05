import challenges


class Decryption(challenges.Challenge):
    # Variables
    prompt = "Hello... its your boss ... we have intellegence on the UT Database. Decrypt these emails and we might " \
             "gain a lead on whos been attacking us...We know this is a Caesar Cipher and the key is 5. "
    points = 0
    timeLimit = 5 * 60
    emailsEncrypted = ["qkdqhb1996z@pryr.frp", "ehuqdugp@ahpqh.frp", "ykdoh@pryr.frp", "ehyorqjkruq@jpdlo.frp"]
    emailsAns = ["nhaney1996w@movo.com", "bernardm@xemne.com", "vhale@movo.com", "bevlonghorn@gmail.com"]

    # Constructor

    def getTimeLimit(self):
        return self.timeLimit

    # Use to access emails and display them in main
    def getEmails(self):
        return self.emailsEncrypted

    # Use this to compare results to user answers, 2 points for correct email
    def getResult(self, userAnwers):
        countCheck = 0
        for x in userAnwers:
            if x in self.emailsAns:
                self.points += 2
                countCheck += 1

        # Bonus point to equal 10 total
        if countCheck == 4:
            self.points += 1
            return True

        return False

    def getPrompt(self):
        return self.prompt
