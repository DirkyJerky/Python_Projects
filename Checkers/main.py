try:
	import sys
	import random as r
	import math
	import os
	import getopt
	import pygame
	from socket import *
	from pygame.locals import *
except ImportError, err:
	print "couldn't load module. %s" % (err)
	sys.exit(2)

### GLOBAL ###
RED = "red"
BLACK = "black"
EMPTY = None
def convert_cords(x2,y2):
	x = 64+(x2)
	y = 64+64+(y2)
	return x,y
def load_png(name):
	""" Load image and return image object"""
	fullname = os.path.join('data', name)
	try:
		image = pygame.image.load(fullname)
		if image.get_alpha() is None:
			image = image.convert()
		else:
			image = image.convert_alpha()
	except pygame.error, message:
		print 'Cannot load image:', fullname
		raise SystemExit, message
	return image
def getNewBoard():
	board = {}
	for y in range(8):
		for x in range(8):
			if (x == 0 or x == 3 or x == 5 or x == 7) and (y == 0 or y == 1 or y == 2):
				board["%d%d"%(x,y)] = ["black",x,y]
			elif (x == 0 or x == 3 or x == 5 or x == 7) and (y == 5 or y == 6 or y == 7):
				board["%d%d"%(x,y)] = ["red",x,y]
			else:
				board["%d%d"%(x,y)] = ["empty",x,y]
	return board
		

def main():
	global FPSCLOCK, REDPIECEIMG ,BLACKPIECEIMG ,BOARDBLACK,BOARDRED
	global SCREEN
	# Screen
	pygame.init()
	FPSCLOCK = pygame.time.Clock()
	SCREEN = pygame.display.set_mode((640,640))
	pygame.display.set_caption('Checkers')
	REDPIECEIMG = load_png("Red_Piece.png")
	BLACKPIECEIMG = load_png("Black_Piece.png")
	BOARDBLACK = load_png("blacksquare.png")
	BOARDRED = load_png("redsquare.png")

	rungame()

def rungame():
	turn = r.choice([RED,BLACK])
	mainboard = getNewBoard()
	drawboard(mainboard)
	while True:
		# Keep looping until player clicks the mouse or quits.
		drawboard(mainboard)
		pygame.display.update()
		FPSCLOCK.tick()
		for event in pygame.event.get(): # event handling loop
			if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONUP:
				return

def drawboard(board):
	SCREEN.fill((255,255,255))
	#draw tiles
	keys = board.keys()
	spacerect = Rect(0,0,64,64)
	for item in keys:
		temp = board[item]
		x,y = convert_cords(temp[1],temp[2])
		spacerect.topleft = (x,y)
		if temp[0] == "red":
			SCREEN.blit(BOARDRED,spacerect)
		else:
			SCREEN.blit(BOARDBLACK,spacerect)








if __name__ == '__main__':
    main()