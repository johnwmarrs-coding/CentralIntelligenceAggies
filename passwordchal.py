import challenges
import re 

class Password(challenges.Challenge):
    prompt1 = "Please guess the password according to the hint"
    prompt2 = "Please enter the new password"
    hint = ["CHARGE","CELLPHONE","LITHIUM"]
    points = 0
    numAnswered = 0
    answer = "battery"

    def showhint(self):
        hints = "The hints are\n"
        #print("The hints are:")
        for i in range(len(self.hint)):
            hints += self.hint[i] + '\n'

        return hints
        
    def getAnswer(self,userAnswer):
        self.numAnswered += 1
        if(userAnswer == self.answer):
            self.points += 5
            return("Bingo!")
        else:
            return ("Sorry, you do not get it right, the right answer is " + self.answer);
            
    def passwordStrength(self,userpassword):
        score = 0
        if (len(userpassword)>8): 
            score += 10
        else:
            result = "weak"
            return result
        if re.search("[a-z]", userpassword): 
            score += 20
        if  re.search("[A-Z]", userpassword): 
            score += 20
        if re.search("[0-9]", userpassword): 
            score += 20
        if  re.search("[_@$]", userpassword): 
            score += 30
        result = ""
        if score > 70:
            self.points += 5
            result = "strong"
        elif score <= 70 and score >= 50:
            result = "median"
            self.points += 3
        else:
            result = "weak"
        return result

    def getPointTotal(self):
        return self.points

    def getPrompt(self):
        if (self.numAnswered == 0):
            return self.prompt1 + '\n' + self.showhint()

        elif (self.numAnswered == 1):
            return self.prompt2
        
#p = Password()
#p.showhint();
#answer = input("Enter the answer: ")
#result1 = p.getAnswer(answer)
#password1 = input("Enter the new password: ")
#result2 = p.password_strength(password1)
#print(result2)