import challenges


class PhishingChallenge(challenges.Challenge):

    #Variables
    points = 10

    prompt = "Hey IT person, I got these emails the other day but I am not sure if I should trust them, what do you think?"

    emails = [
        (
            "Sender: promotions@amazone.com"
            "Recipient: professorSharon@howdyhackuniversity.com"

            "Hello Trusted User,"
            ""
            "Sign up this week only to receive 1 year of free prime membership."
            "This is an exclusive offer given only to our most trusted members."
            "Just log-in here to receive free shipping!"
            "https://amazone.com/freestuffpromo/"  
            ""
            "Thank you for your business!"
            "- Amazon Marketing Team"
        ),

        (
            "Sender: willjames@howdyhackuniversity.edu"
            "Recipient: professorSharon@howdyhackuniversity.edu"

            "Howdy Professor Sharon,"
            ""
            "I was doing research on the basket weaving assignment posted last week."
            "I came across a few interesting websites that I would like you to check out."
            "Let me know what you think of them!"
            ""  
            "https://en.wikipedia.org/wiki/Basket_weaving"
            "https://en.wikipedia.org/wiki/Underwater_basket_weaving"
            ""
            "Thank you for being such a great professor!"
            "- Will James HHU Class of 2022"
        ),

        (
            "Sender: trustedassociate@datacollectionservice.com"
            "Recipient: professorSharon@howdyhackuniversity.com"
            ""
            "IMPORT REMINDER!"
            ""
            "According to new government policy, every citizen needs to update their Social Security Number."
            "If your SSN is not uploaded within the week, then you will be taxed DOUBLE in the upcoming season."
            "ACT NOW TO UPDATE YOUR SSN"
            ""
            "http://datacollectionservice.com/upload"
            ""
            "- US Government Data Collection Service"

        
        )

    ]

    # Answers question, should I trust this email?
    answers = [False, True, False]

    keyInfo = "hacker's website: amazone.com"

    #Constructor

    def getPrompt(self):
    	return self.prompt

    def getResult(self, userAnswer):

        pointsEarned = 0
        answersCorrect = 0

        for i in range(0, len(self.emails)):
            if userAnswer[i] == self.answers[i]:
                answersCorrect +=1

        if (answersCorrect == 3):
            pointsEarned = 10
        elif (answersCorrect == 2):
            pointsEarned = 6
        elif (answersCorrect == 1):
            pointsEarned = 3
        else:
            pointsEarned = 0

    	return pointsEarned

    def getKeyInfo(self):
    	return self.keyInfo
