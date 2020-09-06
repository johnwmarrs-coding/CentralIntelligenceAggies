import challenges


class SQLInject(challenges.Challenge):

    # Variables

    prompt = "Perhaps you can perform SQLInjection on the suspected website to discover the true identity of the person hacking us."
    resource = "https://www.w3schools.com/sql/sql_injection.asp"

    response = ("index, firstName, lastName, username\n0, Charles, Barkley, cbarkley1\n1, Jordan, Michaels, theBigJorms\n"
    "2, Hannah, Hannadotir, theRealHannah\n" 
    "3, George, Andwell, animalFarmed2\n" 
    "4, Henrietta, Andrews, henandrews1998\n" 
    "5, Bevo, Longhorn, bvbandit1\n"
    "6, Rebecca, Beckinson, Rebeckinson420"
    )


    username = 'bvbandit1'
    keyInfo = 'Bevo Longhorn'
    answer = "OR 1=1" 

    # Constructor

    def getPrompt(self):
        return self.prompt

    def getResult(self, userAnswer):
    	if (self.answer.replace(" ", "").lower() == userAnswer.replace(" ", "").lower()):
    		return 10
    	else:
    		return 0

    def getResource(self):
    	return self.resource

    def getResponse(self):
    	return self.response