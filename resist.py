import os, sys
from random import shuffle

numPlayers = input("Please enter the number of players (5-10): ")

missionNumbers = {5: [2, 3, 2, 3, 3], 6: [2, 3, 4, 3, 4], 7: [2, 3, 3, 4, 4], 8: [3, 4, 4, 5, 5], 9: [3, 4, 4, 5, 5], 10: [3, 4, 4, 5, 5]}

roles = {5: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'MORGANA', 'ASSASSIN'], 6: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN'], 7: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 8: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 9: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY'], 10: ['MERLIN', 'PERCIVAL', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'RESISTANCE', 'MORGANA', 'ASSASSIN', 'SPY', 'SPY']}

print roles[numPlayers]
assignRoles = shuffle(roles[numPlayers])
print assignRoles

for i in range(numPlayers):
	print assignRoles[i]
	hide = input("Type Y to continue")
	if hide:
		print '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'

