import challenges


class SQLChallenge(challenges.Challenge):

    # Variables

    prompt = ("We discovered the person hacking us has their own database.\n"
            "I figured out way to access the DB using a backdoor, but\n"
            "I can't figure out a query to get the hackers real name.\n"
            "Could you send me a query to get First Name and Last name of the hacker?\n"
            "I think the db has the following schema:\n\n"
            "USERS(userId, firstName, lastName, username)\n\n"
            "If you need 'Help' let me know\n"
            "Type in the query to get the info I need."
        )

    resource = "https://www.w3schools.com/sql/"

    response = ("index, firstName, lastName, username\n0, Charles, Barkley, cbarkley1\n1, Jordan, Michaels, theBigJorms\n"
    "2, Hannah, Hannadotir, theRealHannah\n" 
    "3, George, Andwell, animalFarmed2\n" 
    "4, Henrietta, Andrews, henandrews1998\n" 
    "5, Bevo, Longhorn, bvbandit1\n"
    "6, Rebecca, Beckinson, Rebeckinson420"
    )


    username = 'bvbandit1'
    keyInfo = 'Bevo Longhorn'
    answer = "SELECT firstName, lastName FROM USERS WHERE username='bvbandit1'"

    tries = 0

    # Constructor

    def getPrompt(self):
        return self.prompt

    def getResult(self, userAnswer):
        self.tries += 1
        userAnswer = userAnswer.replace(';', '')
        print(self.answer.replace(" ", "").lower())
        print(userAnswer.replace(" ", "").lower())
        if (self.answer.replace(" ", "").lower() == userAnswer.replace(" ", "").lower()):
            return True
        else:
            return False

    def getPoints(self):
        if (self.tries <= 2):
            return 10
        elif (self.tries <=3):
            return 6
        elif (self.tries <= 5):
            return 2
        else:
            return 0


    def getResource(self):
    	return self.resource

    def getResponse(self):
    	return self.response

    def getKeyInfo(self):
        return self.keyInfo
