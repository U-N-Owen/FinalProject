'''
The brains for the MasterMind.py program
This file includes a class for one game.
'''

from random import randint

class GameOver(Exception):
		'''
		An exception that I can call when the game has ended.
		Keep in mind, DON'T use this to figure out when the game ends. Because the interface
		needs to keep track of stuff by itself. Anyway, enjoy n' stuff.
		'''
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

class mastermindGame(object):
	'''
	The main brain for the mastermind game,
	Trust me, this code is totally not lame.
	Some other sentence that rhymes with fame.
	And if you break something, you get the blame.
	'''
	def play(self, moves):
		'''
		Call it via something like this:
			myAwesomeMastermindGame.play([7, 5, 9, 2])
		What it returns, a tuple.
			(black pegs, white pegs)
		black pegs are both color AND position correct
		white pegs are JUST color correct
		Enjoy.
		'''
		if self.__plays == self.__rows:
			raise GameOver("THE GAME IS OVER. STOP TRYING TO PLAY ALREADY.")
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
		if b == 4:
			self.__plays = self.__rows
		
		for c in moves:
			while c in code:
				w += 1
				code.remove(c)

		return (b, w)
		
	def turns(self):
		'''
		Returns the number of turns that have gone by.
		Wooeeep!
		'''
		return self.__plays

	def __init__(self, colors, rows):
		self.__colors	= int(colors)
		self.__rows		= int(rows)
		self.__plays	= 0
		self.__code		= (randint(0,self.__colors), randint(0,self.__colors), randint(0,self.__colors), randint(0,self.__colors))
