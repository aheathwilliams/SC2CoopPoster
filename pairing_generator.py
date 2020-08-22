import yaml
import itertools
from commander import Commander

commanders = []

def getCommanders():
	global commanders
	if(commanders):
		return commanders

	myFile = open("config.yml", "r")

	myYaml = yaml.safe_load(myFile)

	myFile.close()

	for commander, details in myYaml["commanders"].items():
		commanders.append(Commander(commander, details))

	return commanders

def getCompletePairings():
	return list(itertools.combinations(getCommanders(),2))

def getNewCommanderPairings(commanderName = ""):
	# if no commanderName was supplied, last entry in commanders is assumed to be the new one
	if(not commanderName):
		newCommander = getCommanders()[-1]
	else:
		for commander in getCommanders():
			if commander.name == commanderName:
				newCommander = commander
				break

	oldCommanderList = filter(lambda com: com != newCommander, getCommanders())

	return list(itertools.product([newCommander], oldCommanderList))
