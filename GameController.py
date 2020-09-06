
import phishingchal as pc
import passwordchal as pac
import maninmiddle as mm
import ddoschal as dds
import player
import random

class GameController:
	terminalFrame = None
	chatFrame = None
	serverFrame = None

	gameState = 2
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
				#You have emails to read still
				self.chatFrame.handleReceiveMessage(self.phishingChallenge.getEmail(), "Boss")

			else:
				self.chatFrame.handleReceiveMessage("You got " + str(response) + " points", "Boss")
				self.player.addPoints(response)

				self.gameState += 1
				#self.displayPasswordChallenge()
				self.displayGameState()

		if (self.gameState == 1):
			if (self.passwordChallenge.numAnswered == 0):
				response = self.passwordChallenge.getAnswer(updateInput)
				self.terminalFrame.handleReceiveOutput(response, "system")

				self.terminalFrame.handleReceiveOutput(self.passwordChallenge.getPrompt(), "system")
			elif (self.passwordChallenge.numAnswered == 1):
				response = self.passwordChallenge.passwordStrength(updateInput)
				self.terminalFrame.handleReceiveOutput(response, "system")

				self.player.addPoints(self.passwordChallenge.getPointTotal())
				self.gameState += 1

		if (self.gameState == 2):
			print(updateInput.lower())
			if (updateInput.lower() == 'done'):
				response = self.ddosChallenge.getResult()
				self.player.addPoints(response)
				if (response == 10):
					self.chatFrame.handleReceiveMessage("You stopped all of the hackers in the attack. Great job!", "Boss")
				else:
					self.chatFrame.handleReceiveMessage("You tried, but I can only give you a " + str(response) + "/10 for that performance.", "Boss")
			elif (updateInput.lower() == 'help'):
				print('And not this')
				self.chatFrame.handleReceiveMessage("Look for ip's that don't behave naturally and block them.", "Boss")
			else:
				print('Did this')
				if (isinstance(updateInput, str)):
					self.ddosChallenge.answer(updateInput)
				else:
					print('Not sure what to do with that info')


		if (self.gameState == 4):
			if (self.manInMiddle.getResult(updateInput)):
				self.chatFrame.handleReceiveMessage("My goodness you cracked it! Buddy ole chap!", "Boss")
				self.player.addPoints(self.manInMiddle.getPoints())
				self.gameState += 1
			else:
				self.chatFrame.handleReceiveMessage("Hmmm. That doesn't seem quite right. Keep trying!", "Boss")

	def displayGameState(self):
		print('Displaying game state')
		if (self.gameState == 0):
			self.displayPhishingChallenge()
		elif (self.gameState == 1):
			self.displayPasswordChallenge()
		elif (self.gameState == 2):
			self.displayDDOSChallenge()
		elif (self.gameState == 4):
			self.displayManInMiddleChallenge()



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

		self.chatFrame.handleReceiveMessage("Some users are reporting that they can't access the howdyhack website, can you check the server?", "Boss")
		self.chatFrame.handleReceiveMessage("Let me know when you are 'Done' or if you need 'Help'.", "Boss")

		alert = self.ddosChallenge.getAlert()
		self.serverFrame.setAlert(alert, "red")

		self.ipList = []
		self.ipList = self.ipList + self.ddosChallenge.getNoiseIps()
		self.ipList = self.ipList + self.ddosChallenge.getIpsToBlacklist()

		self.data = []
		for i in range(0, len(self.ipList)):
			if (i < len(self.ipList)-3):
				self.data.append((self.ipList[i], random.randrange(1, 50)))
			else:
				self.data.append((self.ipList[i], random.randrange(5000, 25000)))

		self.serverFrame.setIps(self.data)


	def setTerminalFrame(self, tf):
		self.terminalFrame = tf

	def setChatFrame(self, cf):
		self.chatFrame = cf

	def setServerFrame(self, sf):
		self.serverFrame = sf

