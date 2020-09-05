import challenges


class Encryption(challenges.Challenge):
    # Variables
    points = 10
    prompt = "You suspect that somobody might be listening to this message...\nEncrypt this message with Caesar " \
             "Cipher to hide this message... 'Sombody has the password to the hackathon site, please change it.' "
    ans = "Xtrgtid mfx ymj ufxxbtwi yt ymj mfhpfymts xnyj, uqjfxj hmfslj ny."

    # Constructor
    def getPrompt(self):
        return self.prompt

    def getResult(self, userAns):
        if userAns.lower() == self.ans.lower():
            return True
        else:
            return False
