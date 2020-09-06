import phishingchal as pc
import passwordchal as pac
import maninmiddle as mm
import ddoschal as dds
import sqlchal as sc
import player
import random

class GameController:
    terminalFrame = None
    chatFrame = None
    serverFrame = None

    gameState = 0
    player = None

    def __init__(self):
        print("The cybersecurity game is a go! go! g0!")
        self.player = player.Player()

    def startGame(self):

        self.displayGameState()

    def updateGame(self, updateInput):
        print("Updating game")

        if (self.gameState == 0):
            # Process the update as if it was meant to solve the current state
            response = self.phishingChallenge.provideAnswer(updateInput)
            if (response == None):
                # You have emails to read still
                self.chatFrame.handleReceiveMessage(self.phishingChallenge.getEmail(), "Boss")

            else:
                self.chatFrame.handleReceiveMessage("Ok I've got your answers. Thanks for the help...", "Boss")
                self.player.addPoints(response)
                self.chatFrame.handleReceiveMessage(
					"*Its the next day, you feel like you answered a phishing email wrong* You might want to create a new strong password in terminal.",
					"System")

                self.gameState += 1
                # self.displayPasswordChallenge()
                self.displayGameState()

        elif (self.gameState == 1):
            if (self.passwordChallenge.numAnswered == 0):
                response = self.passwordChallenge.getAnswer(updateInput)
                self.terminalFrame.handleReceiveOutput(response, "system")

                self.terminalFrame.handleReceiveOutput(self.passwordChallenge.getPrompt(), "system")
            elif (self.passwordChallenge.numAnswered == 1):
                response = self.passwordChallenge.passwordStrength(updateInput)
                self.terminalFrame.handleReceiveOutput(response, "system")

                self.player.addPoints(self.passwordChallenge.getPointTotal())
                self.gameState += 1
                self.displayGameState()

        elif (self.gameState == 3):
            print(updateInput.lower())
            if (updateInput.lower() == 'done'):
                response = self.ddosChallenge.getResult()
                self.player.addPoints(response)
                if (response == 10):
                    self.chatFrame.handleReceiveMessage("You stopped all of the packet influx to our network. Great job!",
                                                        "Boss")
                    self.gameState += 1
                    self.displayGameState()
                else:
                    self.chatFrame.handleReceiveMessage(
                        "You tried, but I can only give you a " + str(response) + "/10 for that performance.", "Boss")
                    self.chatFrame.handleReceiveMessage("You failed to save howdy hack. You are fired! (YOU LOSE)",
                                                        "Boss")

            elif (updateInput.lower() == 'help'):
                print('And not this')
                self.chatFrame.handleReceiveMessage("Look for ip's that don't behave naturally and block them.", "Boss")
            else:
                print('Did this')
                if (isinstance(updateInput, str)):
                    self.ddosChallenge.answer(updateInput)
                else:
                    print('Not sure what to do with that info')


        elif (self.gameState == 2):
            if (self.manInMiddle.getResult(updateInput)):
                self.chatFrame.handleReceiveMessage("My goodness you cracked it! Buddy ole chap! *Key info discovered*", "Boss")
                self.player.addPoints(self.manInMiddle.getPoints())

                self.keyInfoFrame.addKeyInfo('hacker username:' + self.manInMiddle.getKeyInfo())


                self.gameState += 1
                self.displayGameState()
            else:
                self.chatFrame.handleReceiveMessage("Hmmm. That doesn't seem quite right. Keep trying!", "Boss")

        elif self.gameState == 4:
            if updateInput.lower() == 'help':
                self.chatFrame.handleReceiveMessage('Take a look at this: ' + str(self.sqlChallenge.getResource()),
                                                    "Boss")
            else:
                response = self.sqlChallenge.getResult(updateInput)
                print(updateInput)
                if response:
                    self.chatFrame.handleReceiveMessage('The query returned Bevo, Longhorn...', "Boss")
                    self.chatFrame.handleReceiveMessage('That must be the hacker! TU meddling with us again!', "Boss")
                    self.chatFrame.handleReceiveMessage('That query worked! You found the person hacking us!', "Boss")
                    self.chatFrame.handleReceiveMessage(
                        'I can notify the authorities to prevent ' + self.sqlChallenge.getKeyInfo() + ' from hacking us ever again!',
                        "Boss")
                    self.player.addPoints(self.sqlChallenge.getPoints())

                    self.chatFrame.handleReceiveMessage('You finished the game!', "Boss")
                    self.chatFrame.handleReceiveMessage('You earned a total of ' + str(self.player.points) + " points", "Boss")
                    self.chatFrame.handleReceiveMessage('This makes you: ' + str(self.player.calculateTitle()), "Boss")

                    self.gameState += 1
                elif response == False:
                    self.chatFrame.handleReceiveMessage("That didn't work, try giving it another go.", "Boss")

    def displayGameState(self):
        print('Displaying game state')
        if (self.gameState == 0):
            self.displayPhishingChallenge()
        elif (self.gameState == 1):
            self.displayPasswordChallenge()
        elif (self.gameState == 2):
            self.displayManInMiddleChallenge()
        elif (self.gameState == 3):
            self.displayDDOSChallenge()
        elif (self.gameState == 4):
            self.displaySQLChallenge()

    def displayPhishingChallenge(self):
        self.phishingChallenge = pc.PhishingChallenge()

        self.chatFrame.handleReceiveMessage(self.phishingChallenge.getPrompt(), "Boss")
        self.chatFrame.handleReceiveMessage(self.phishingChallenge.getEmail(), "Boss")

    def displayPasswordChallenge(self):
        print('Displaying challenge')
        self.passwordChallenge = pac.Password()

        self.terminalFrame.handleReceiveOutput(self.passwordChallenge.getPrompt(), "system")

    def displayManInMiddleChallenge(self):
        print('Displaying man in middle')
        self.manInMiddle = mm.ManInMiddle()

        self.chatFrame.handleReceiveMessage(self.manInMiddle.getPrompt(), "Boss")
        self.chatFrame.handleReceiveMessage(self.manInMiddle.getIntercept(), "Boss")

    def displayDDOSChallenge(self):
        print("Displaying DDOS challenge")
        self.ddosChallenge = dds.DDOSChallenge()

        self.chatFrame.handleReceiveMessage(
            "Some users are reporting that they can't access the howdyhack website, can you check the server?", "Boss")
        self.chatFrame.handleReceiveMessage("Let me know when you are 'Done' or if you need 'Help'.", "Boss")

        alert = self.ddosChallenge.getAlert()
        self.serverFrame.setAlert(alert, "red")

        self.ipList = []
        self.ipList = self.ipList + self.ddosChallenge.getNoiseIps()
        self.ipList = self.ipList + self.ddosChallenge.getIpsToBlacklist()

        self.data = []
        for i in range(0, len(self.ipList)):
            if (i < len(self.ipList) - 3):
                self.data.append((self.ipList[i], random.randrange(1, 50)))
            else:
                self.data.append((self.ipList[i], random.randrange(5000, 25000)))

        random.shuffle(self.data)
        self.serverFrame.setIps(self.data)

    def displaySQLChallenge(self):
        print("Displaying sql chal")

        self.sqlChallenge = sc.SQLChallenge()

        prompt = self.sqlChallenge.getPrompt()
        self.chatFrame.handleReceiveMessage(prompt, "Boss")

    def setTerminalFrame(self, tf):
        self.terminalFrame = tf

    def setChatFrame(self, cf):
        self.chatFrame = cf

    def setServerFrame(self, sf):
        self.serverFrame = sf

    def setKeyInfoFrame(self, kif):
        self.keyInfoFrame = kif
