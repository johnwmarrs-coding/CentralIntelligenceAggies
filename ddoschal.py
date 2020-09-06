import challenges


class DDOSChallenge(challenges.Challenge):

    #Variables
    points = 10

    prompt = "Users are reporting that they cannot access the howdyhack website for registration. Can you look into the issue? It might be a DOS attack. Maybe you can block some IPs"

    ipsToBlacklist = ["153.65.230.21", "301.78.712.11", "120.78.712.31"]

    keyInfo = "Attacker IPs = '153.65.230.21', '301.78.712.11', '120.78.712.31'"

    #Constructor

    def runchal(self):
        print("### DDOS Challenge ###")

    def getPrompt(self):
    	return self.prompt

    def getResult(self, userAnswer):
    	hits = 0
    	misses = 0

    	tempIpsToBlacklist = self.ipsToBlacklist.copy()
    	for ip in userAnswer:
    		if(ip in tempIpsToBlacklist):
    			tempIpsToBlacklist.remove(ip)
    			hits += 1

    		else:
    			misses += 1

    	pointsEarned = 0
    	if (hits == 3):
    		pointsEarned = 6
    	elif (hits == 2):
    		pointsEarned = 4
    	elif (hits == 1):
    		pointsEarned = 2

    	if (misses == 0):
    		pointsEarned += 4

    	return pointsEarned

    def getKeyInfo(self):
    	return self.keyInfo
