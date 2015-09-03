import os, sys
from random import shuffle

numPlayers = int(raw_input("Please enter the number of players (5-10): "))

missionNumbers = {5: [2, 3, 2, 3, 3], 6: [2, 3, 4, 3, 4], 7: [2, 3, 3, 4, 4], 8: [3, 4, 4, 5, 5], 9: [3, 4, 4, 5, 5], 10: [3, 4, 4, 5, 5]}

roles = {5: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'MORGANA', 'ASSASSIN'], 6: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN'], 7: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 8: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 9: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 10: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY', 'SPY']}

assignRoles = roles[numPlayers]
shuffle(assignRoles)

for i in range(numPlayers):
	printNext = raw_input("Player " + str(i + 1) + ": Press Enter to reveal your role ")
	if str(printNext) == "":
		print assignRoles[i]
	hide = raw_input("Press Enter to hide your role ")
	if str(hide) == "":
		os.system('clear')
