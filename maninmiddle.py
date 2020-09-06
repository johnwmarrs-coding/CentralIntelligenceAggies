import challenges


class ManInMiddle(challenges.Challenge):

    # Variables
    prompt = "Its your boss again ... we have intercepted Bevo's messages sent to a 2 percenter. We need you to " \
             "perform decryption again and steal his login information." \

    points = 0

    interceptMessage = "suhsdulqj wkh ggrv dwwdfn qrz - eyedqglw1!"

    decryptedIntercept = "preparing the ddos attack now - bvbandit1"
    keyInfo = 'bvbandit1'

    def getIntercept(self):
        return self.interceptMessage

    # Use this to access points earned for this challenge after calling getResult()
    
    def getPoints(self):
        return self.points

    def computePoints(self, userResult):
        if self.decryptedIntercept.lower() == userResult.lower():
            self.points = 10

    def getResult(self, userResult):
        if self.decryptedIntercept.lower() == userResult.lower():
            self.computePoints(userResult)
            return True
        else:
            return False

    def getPrompt(self):
        return self.prompt

    def getKeyInfo(self):
        return self.keyInfo


