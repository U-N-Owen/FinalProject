#! /usr/bin/env python

import curses # we need to have a shiny text interface hyar
              # also we need to curse.
import re     # regexs are the best way to do stuff with user input, in my opinion.

stdscr = curses.initscr() # boring initial curses setup
curses.nocbreak(); stdscr.keypad(0); curses.echo() # more boring stuffs

def numInput(message, error=""):
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
	y = ""
	for i in range(0, x):
		y += " "
	stdscr.addstr(0, 0, "You have " + str(turn) + " turns left out of " + str(turns) + " total. You have a total of " + str(colors) + " colors.", curses.A_REVERSE)
	stdscr.addstr(y)

turns = numInput("How many turns do you want to have?")
turn = turns
colors = numInput("How many colors do you want to have?")
while colors < 2:
	colors = numInput("How many colors do you want to have?", "INVALID INPUT")

stdscr.clear()

header(turn, turns, colors)

nextY = 2

# set up the "template" for stuff
temp = " " * len(str(colors-1))
template = "| " + temp + ", " + temp + ", " + temp + ", " + " |   |   |"
del temp
# and shove up a nice line onto the screen :D
stdscr.addstr(1, 0, "-" * len(template))

#while turn != 0 and :
	

curses.endwin()
# pad = curses.newpad(
#while 1:
#	c = stdscr.getch()
#curses.endwin()
