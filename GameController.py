
import phishingchal as pc
import passwordchal as pac
import player

class GameController:
	terminalFrame = None
	chatFrame = None
	serverFrame = None

	gameState = 1
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

	def displayGameState(self):
		print('Displaying game state')
		if (self.gameState == 0):
			self.displayPhishingChallenge()
		elif (self.gameState == 1):
			self.displayPasswordChallenge()



	def displayPhishingChallenge(self):
		self.phishingChallenge = pc.PhishingChallenge()

		self.chatFrame.handleReceiveMessage(self.phishingChallenge.getPrompt(), "Boss")
		self.chatFrame.handleReceiveMessage(self.phishingChallenge.getEmail(), "Boss")

	def displayPasswordChallenge(self):
		print('Displaying challenge')
		self.passwordChallenge = pac.Password()

		self.terminalFrame.handleReceiveOutput(self.passwordChallenge.getPrompt(), "system")

	def setTerminalFrame(self, tf):
		self.terminalFrame = tf

	def setChatFrame(self, cf):
		self.chatFrame = cf

	def setServerFrame(self, sf):
		self.serverFrame = sf

