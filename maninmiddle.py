import challenges


class ManInMiddle(challenges.Challenge):

    # Variables
    prompt = "Its your boss again ... we have intercepted Bevo's messages sent to a 2 percenter. We need you to " \
             "perform decryption again and steal his login information." \

    points = 0

    interceptMessage = "Odxqfk wkh udqvrpzduh!"

    decryptedIntercept = "Launch the ransomware!"

    def getIntercept(self):
        return self.interceptMessage

    # Call this after get result because points get set after get result
    def getPoints(self):
        return self.points

    def computePoints(self, userResult):
        if self.decryptedIntercept.lower == userResult.lower:
            self.points = 10

    def getResult(self, userResult):
        if self.decryptedIntercept.lower == userResult.lower:
            self.computeResult(userResult)
            return True


