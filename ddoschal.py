import challenges


class DDOSChallenge(challenges.Challenge):

    #Variables
    points = 10

    prompt = "Users are reporting that they cannot access the howdyhack website for registration. Can you look into the issue? It might be a DOS attack. Maybe you can block some IPs"
    alert = "SERVING RECEIVING HIGH TRAFFIC"

    noiseIps = [  "342.32.323.23",
                "324:32:323:32",
                "127.00.121.21",
                "127.00.000.01",
                "632.13.322.12",
                "321.12.123.21",
                "221.32.233.32",
                "420.69.420.69"]
    ipsToBlacklist = ["153.65.230.21", "301.78.712.11", "120.78.712.31"]

    keyInfo = "Attacker IPs = '153.65.230.21', '301.78.712.11', '120.78.712.31'"

    userAnswer = []

    #Constructor

    def runchal(self):
        print("### DDOS Challenge ###")

    def getPrompt(self):
    	return self.prompt

    def getResult(self):
    	hits = 0
    	misses = 0

    	tempIpsToBlacklist = self.ipsToBlacklist.copy()
    	for ip in self.userAnswer:
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

    def answer(self, ans):
        self.userAnswer.append(ans)


    def getKeyInfo(self):
    	return self.keyInfo

    def getAlert(self):
        return self.alert;

    def getNoiseIps(self):
        return self.noiseIps

    def getIpsToBlacklist(self):
        return self.ipsToBlacklist

