import os, sys
from random import shuffle
import getpass

numPlayers = int(raw_input("Please enter the number of players (5-10): "))
players = []

for i in range(numPlayers):
	playerName = raw_input("Player " + str(i + 1) + " please enter your name: ")
	players.append(playerName)

missionNumbers = {5: [2, 3, 2, 3, 3], 6: [2, 3, 4, 3, 4], 7: [2, 3, 3, 4, 4], 8: [3, 4, 4, 5, 5], 9: [3, 4, 4, 5, 5], 10: [3, 4, 4, 5, 5]}

roles = {5: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'MORGANA', 'ASSASSIN'], 6: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN'], 7: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 8: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 9: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 10: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY', 'SPY']}

assignRoles = roles[numPlayers]
shuffle(assignRoles)

for i in range(numPlayers):
	printNext = raw_input(players[i] + ": Press Enter to reveal your role ")
	if str(printNext) == "":
		print assignRoles[i]
	hide = raw_input("Press Enter to hide your role ")
	if str(hide) == "":
		os.system('clear')

shuffle(players)
print players[0] + " starts, " + players[4 % numPlayers] + " is hammer.\n"
currentPlayer = 0

for i in range(5):
	numOnMission = missionNumbers[numPlayers][i]
	proposalNumber = 1
	passedMission = False
	while not passedMission:
		proposedTeam = []
		for j in range(numOnMission):
			proposedTeam.append(raw_input(players[currentPlayer] + ", please choose a person to go on your mission: "))
		votes = []
		yesVotes = 0
		for j in range(numPlayers):
			currentVote = getpass.getpass(players[j] + ", please vote on the proposed team (Y/N): ")
			votes.append(currentVote)
			if currentVote == 'Y':
				yesVotes += 1
		for player, vote in zip(players, votes):
			print player + ": " + vote + "\n"
		if yesVotes/numPlayers > 0.5:
			print "The proposed team passes."
			passedMission = True
		else:
			print "The proposed team fails."
		if proposalNumber > 5:
			passedMission = True
		proposalNumber += 1
		currentPlayer = (currentPlayer + 1) % 5

