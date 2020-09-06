import challenges


class PhishingChallenge(challenges.Challenge):

    #Variables
    points = 10

    prompt = "Hey IT person, I got these emails the other day but I am not sure if I should trust them, what do you think?"

    numberAnswered = 0
    userAnswer = []

    emails = [
        (
            "\nSender: promotions@amazone.com\n"
            "Recipient: professorSharon@howdyhackuniversity.com\n"
            "\n"
            "Hello Trusted User,\n"
            "\n"
            "Sign up this week only to receive 1 year of free prime membership.\n"
            "This is an exclusive offer given only to our most trusted members.\n"
            "Just log-in here to receive free shipping!\n\n"
            "https://amazone.com/freestuffpromo/\n"  
            "\n"
            "Thank you for your business!\n"
            "- Amazon Marketing Team\n"
        ),

        (
            "Sender: willjames@howdyhackuniversity.edu\n"
            "Recipient: professorSharon@howdyhackuniversity.edu\n"

            "Howdy Professor Sharon,\n"
            "\n"
            "I was doing research on the basket weaving assignment posted last week.\n"
            "I came across a few interesting websites that I would like you to check out.\n"
            "Let me know what you think of them!\n"
            ""  
            "https://en.wikipedia.org/wiki/Basket_weaving\n"
            "https://en.wikipedia.org/wiki/Underwater_basket_weaving\n"
            ""
            "Thank you for being such a great professor!\n"
            "- Will James HHU Class of 2022\n"
        ),

        (
            "Sender: trustedassociate@datacollectionservice.com\n"
            "Recipient: professorSharon@howdyhackuniversity.com\n"
            "\n"
            "IMPORT REMINDER!\n"
            ""
            "According to new government policy, every citizen needs to update their Social Security Number.\n"
            "If your SSN is not uploaded within the week, then you will be taxed DOUBLE in the upcoming season.\n"
            "ACT NOW TO UPDATE YOUR SSN\n"
            ""
            "http://datacollectionservice.com/upload\n"
            ""
            "- US Government Data Collection Service\n"

        
        )

    ]

    # Answers question, should I trust this email?
    answers = [False, True, False]

    keyInfo = "hacker's website: amazone.com"

    # Constructor

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

    def getEmail(self):
        return self.emails[self.numberAnswered]


    def provideAnswer(self, ans):
        if (ans.lower() == "yes"):
            self.numberAnswered += 1
            self.userAnswer.append(True)
        elif (ans.lower() == "no"):
            self.numberAnswered += 1
            self.userAnswer.append(False)
        else:
            return "I don't understand your answer"

        if (self.numberAnswered == len(self.emails)):
            return self.getResult(self.userAnswer)
        else:
            return None


