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

turns = numInput("How many turns do you want to have?")
colors = numInput("How many colors do you want to have?")

stdscr.clear()



while 1:
	

curses.endwin()
# pad = curses.newpad(
#while 1:
#	c = stdscr.getch()
#curses.endwin()
