import os, sys
from random import shuffle
import getpass

os.system('clear')
numPlayers = int(raw_input("Please enter the number of players (5-10): "))
players = []

for i in range(numPlayers):
	playerName = raw_input("Player " + str(i + 1) + " please enter your name: ")
	players.append(playerName)
os.system('clear')

missionNumbers = {5: [2, 3, 2, 3, 3], 6: [2, 3, 4, 3, 4], 7: [2, 3, 3, 4, 4], 8: [3, 4, 4, 5, 5], 9: [3, 4, 4, 5, 5], 10: [3, 4, 4, 5, 5]}

roles = {5: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'MORGANA', 'ASSASSIN'], 6: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN'], 7: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 8: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 9: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 10: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY', 'SPY']}

assignRoles = roles[numPlayers]
shuffle(assignRoles)
rememberRoles = {}

for i in range(numPlayers):
	currentPlayer = players[i]
	printNext = raw_input(currentPlayer + ": Press Enter to reveal your role ")
	if str(printNext) == "":
		currentRole = assignRoles[i]
		print currentRole
		rememberRoles[currentRole] = currentPlayer
	hide = raw_input("Press Enter to hide your role ")
	if str(hide) == "":
		os.system('clear')

shuffle(players)
currentPlayer = 0
score = {'R': 0, 'S': 0}
win = 0

for i in range(5):
	print "MISSION " + str(i + 1) + '\n'
	print players[currentPlayer] + " starts, " + players[(currentPlayer + 4) % numPlayers] + " is hammer.\n\n"
	numOnMission = missionNumbers[numPlayers][i]
	proposalNumber = 1
	passedMission = False
	while not passedMission:
		proposedTeam = []
		for j in range(numOnMission):
			proposedTeam.append(raw_input(players[currentPlayer] + ", please choose a person to go on your mission: "))
		print '\n'
		votes = []
		yesVotes = 0
		for j in range(numPlayers):
			currentVote = getpass.getpass(players[j] + ", please vote on the proposed team (Y/N): ")
			votes.append(currentVote)
			if currentVote == 'Y':
				yesVotes += 1
		print '\n'
		for player, vote in zip(players, votes):
			print player + ": " + vote + "\n"
		if float(yesVotes)/float(numPlayers) > 0.5:
			passedMission = True
		else:
			print "The proposed team fails."
		if proposalNumber > 5:
			passedMission = True
		proposalNumber += 1
		currentPlayer = (currentPlayer + 1) % 5

	temp = raw_input("The proposed team passes. Press enter to proceed to voting.")
	if temp == "":
		os.system('clear')

	numSucceed = 0
	for j in range(numOnMission):
		currentVote = getpass.getpass(proposedTeam[j] + ", do you want to succeed or fail the mission? (S/F): ")
		os.system('clear')
		if currentVote == 'S':
			numSucceed += 1
	numFail = numOnMission - numSucceed
	result = 'succeeded'
	if i == 3 and numFail > 1:
		result = 'failed'
		score['S'] += 1
	elif numFail:
		result = 'failed'
		score['S'] += 1
	else:
		score['R'] += 1

	print "The mission has " + result + ": " + str(numSucceed) + " succeed(s) and " + str(numFail) + " fail(s).\n"

	if score['R'] == 3:
		win = 'R'
		break
	if score['S'] == 3:
		win = 'S'
		print "SPIES WIN!"
		break
	else:
		print "The score is resistance: " + str(score['R']) + ", spies: " + str(score['S']) + "."
	temp = raw_input("Press Enter to proceed ")
	if temp == "":
		os.system('clear')

if win == 'R':
	MerlinGuess = raw_input("The Resistance has won 3 out of 5 missions. Spies, you have one last chance! Correctly guess Merlin to win the game: ")
	if MerlinGuess == rememberRoles['MERLIN']:
		"You have correctly guessed Merlin! SPIES WIN!"
	else:
		"You have incorrectly guessed Merlin. RESISTANCE WINS!"

print "ROLES:\n\n"
for role in assignRoles:
	print role + ": " + rememberRole[role] + "\n\n"
