'''
The brains for the MasterMind.py program
This file includes a class for one game.
'''

from random import randint

class mastermindGame(object):
	def play(self, moves):
		if self.__plays == self.__rows:
			raise("GameShouldHaveEnded")
		self.__plays += 1
		code = list(self.__code)

		w = 0
		b = 0
		
		# there are 4 if statements because a for loop
		# takes up extra time... probably
		if code[3] == moves[3]:
			b += 1
			del code[3:4]
			del moves[3:4]
		if self.__code[2] == moves[2]:
			b += 1
			del code[2:3]
			del moves[2:3]
		if self.__code[1] == moves[1]:
			b += 1
			del code[1:2]
			del moves[1:2]
		if self.__code[0] == moves[0]:
			b += 1
			del code[0:1]
			del moves[0:1]

		for c in moves:
			if c in code:
				w += 1
				moves.remove(c)
				code.remove(c)

		return (b, w)

		
	def __init__(self, colors, rows):
		self.__colors	= int(colors)
		self.__rows		= int(rows)
		self.__plays	= 0
		self.__code		= (randint(0,self.__colors), randint(0,self.__colors), randint(0,self.__colors), randint(0,self.__colors))
