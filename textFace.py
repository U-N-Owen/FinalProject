#! /usr/bin/env python

import curses # we need to have a shiny text interface hyar
              # also we need to curse.
import re     # regexs are the best way to do stuff with user input, in my opinion.

import brains # has to be in the same directory as this file
	
class Template(object):
	def __init__(self):
		self.template = ""
		self.line = ""
		self.offA = 0
		self.offB = 0
		self.offC = 0
		self.offD = 0
		self.pegW = 0
		self.pegB = 0

stdscr = curses.initscr() # boring initial curses setup
curses.nocbreak(); stdscr.keypad(0); curses.echo() # more boring stuffs

# lazy, so imma gonna go with some recursion, mwhahahahahahah!
def numInput(message, error=""):
	'''
	basic number inputing in the beginning
	sure, it sucks, but it works
	'''
	stdscr.clear()
	if error == "":
		n = 0
	else:
		n = 1
		stdscr.addstr(0, 0, error)
	stdscr.addstr(n, 0, message + "\n>")
	num = stdscr.getstr(n+1, 2)
	try:
		num = int(num)
	except:
		return numInput(message, "INVALID INPUT")
	else:
		return num

def header(turn, turns, colors):
	x = len(str(turns)) - len(str(turn))
	# augh, hacky, I know.
	y = ""
	for i in range(0, x):
		y += " "
	stdscr.addstr(0, 0, "You have " + str(turn) + " turns left out of " + str(turns) + " total. You have a total of " + str(colors) + " colors (0 through " + str(colors-1) + " inclusive.)", curses.A_REVERSE)
	stdscr.addstr(y)

def getTurn(nextY, colors):
	stdscr.addstr(nextY + 2, 0, "> ")
	stdscr.addstr(" " * 100) # AAAA! I'M SORRY! I'M SORRY FOR MY HORRIFIC CODE! I SHOULD CHANGE THIS! I SHOULD!!! 
	#
	#
	#
	#
	#    NO, REALLY: Change this code ASAP. Because what if I write a whole bunch? :P
	#
	#    also, what about errors and stuff? JUST CLEAN THIS PART OF THE CODE UP IN GENERAL! REWRITE IT! DO IT!
	#
	#
	#
	#
	inp = stdscr.getstr(nextY + 2, 2)
	if inp == "q":
		return False
	regx = re.match("^[^\d]*(\d+)[^\d]+(\d+)[^\d]+(\d+)[^\d]+(\d+)[^\d]*$", inp) # Oh boy do I love regex! This is the only reason I even included regex here. PARSING INPUT! :D
	try:
		matches = regx.groups()
	except:
		stdscr.addstr(nextY + 3, 0, "NOT VALID INPUT", curses.A_REVERSE) ### &&&@* Yes, it's cheating, making these the same length.
		return getTurn(nextY, colors)
	okay = True
	matches = map(int, matches)
	for match in matches:
		if match >= colors or match < 0:
			okay = False
	if not okay:
		stdscr.addstr(nextY + 3, 0, "INVALID  COLORS", curses.A_REVERSE) ### &&&@* So what?
		return getTurn(nextY, colors)
	return matches

turns = numInput("How many turns do you want to have?")
turn = turns
colors = numInput("How many colors do you want to have?")
while colors < 2:
	colors = numInput("How many colors do you want to have?", "INVALID INPUT")

stdscr.clear()

game = brains.mastermindGame(colors-1, turns)


nextY = 4

# set up the "template" for stuff
template = Template()
temp = " " * len(str(colors-1))
template.template = "| " + temp + ", " + temp + ", " + temp + ", " + temp + " |   |   |"
template.offA = 2
template.offB = template.offA + len(temp) + 2
template.offC = template.offB + len(temp) + 2
template.offD = template.offC + len(temp) + 2
template.pegW = template.offD + len(temp) + 3
template.pegB = template.pegW + 4
template.line = "-" * len(template.template)
del temp
# and shove up a nice line (or two) onto the screen :D
stdscr.addstr(1, 0, template.line)
stdscr.addstr(3, 0, template.line)
# now tell us what the friq this is, sort-of
stdscr.addstr(2, 0, template.template)
stdscr.addstr(2, template.offA, "A")
stdscr.addstr(2, template.offB, "B")
stdscr.addstr(2, template.offC, "C")
stdscr.addstr(2, template.offD, "D")
stdscr.addstr(2, template.pegW, "W")
stdscr.addstr(2, template.pegB, "B")

# ################################################ #
# sure, it's not beautiful, but it'll do, I guess. #
# ################################################ #

# and some more cheap trickery, because I'm lazy
b = 0

message = "lost."

# and the main loop
while turn != 0 and b != 4:
	header(turn, turns, colors)
	usrCode = getTurn(nextY, colors)
	if usrCode == False:
		message = "ended the game early."
		break
	thisPlay = game.play(usrCode)
	b = thisPlay[0]
	stdscr.addstr(nextY, 0, template.template)
	stdscr.addstr(nextY, template.offA, str(usrCode[0]))
	stdscr.addstr(nextY, template.offB, str(usrCode[1]))
	stdscr.addstr(nextY, template.offC, str(usrCode[2]))
	stdscr.addstr(nextY, template.offD, str(usrCode[3]))
	stdscr.addstr(nextY, template.pegW, str(thisPlay[1]))
	stdscr.addstr(nextY, template.pegB, str(thisPlay[0]))
	turn = turns - game.turns()
	stdscr.addstr(nextY + 2, 0, " " * 102) # AGAIN, THIS IS HORRIFIC I MEAN REALLY TRULY HORRIFIC COMPARED TO SOME OF THE THINGS I'VE DONE ABOVE AND BELOW
	nextY += 1

curses.endwin()
if b == 4:
	message = "won!"
print("\nYou " + message + " The code was " + str(game.code()) + ".\n")
