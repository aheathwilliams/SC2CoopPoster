from yaml import safe_load
from itertools import product, combinations
from commander import Commander

commanders = []

def getAllCommanders():
	global commanders
	if(commanders):
		return commanders

	with open("config.yml", "r") as file:
		for commander, details in safe_load(file)["commanders"].items():
			commanders.append(Commander(commander, details))
			
	return commanders

def getCompletePairings():
	return list(combinations(getAllCommanders(),2))

def getNewCommanderPairings(commanderName = ""):
	# if no commanderName was supplied, last entry in commanders is assumed to be the new one
	if(not commanderName):
		newCommander = getAllCommanders()[-1]
	else:
		for commander in getAllCommanders():
			if commander.name == commanderName:
				newCommander = commander
				break

	oldCommanderList = filter(lambda com: com != newCommander, getAllCommanders())

	return list(product([newCommander], oldCommanderList))

